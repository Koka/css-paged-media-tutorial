import os
import sys
import tempfile
import lxml.html
import shutil
import pprint
import commands
import PyPDF2
from lxml.cssselect import CSSSelector


outer_tmpl = """
<div class="outer floatable" id="{id}">
    <div class="inner">
        <div class="wrapper">
        id={id}
        </div>
    </div>
</div>
"""



class Processor(object):

    def __init__(self, input_filename):
        self.input_filename = os.path.abspath(input_filename)
        self.tmpdir = tempfile.mkdtemp()
        self.logfile = os.path.join(self.tmpdir, 'conversion.log')
        self.index_html = os.path.join(self.tmpdir, 'index.html')
        self.index2_html = os.path.join(self.tmpdir, 'index2.html')
        self.index2_pdf= os.path.join(self.tmpdir, 'index2.pdf')
        self.index2_areatree = os.path.join(self.tmpdir, 'index2.areatree')
        self.pdf_final = os.path.join(self.tmpdir, 'final.pdf')
        shutil.copy(input_filename, self.index_html)
        shutil.copytree('styles', os.path.join(self.tmpdir, 'styles'))
        self._log('copied {} -> {}'.format(self.input_filename, self.index_html))

    def _log(self, message, level='info'):
        print message
        with open(self.logfile, 'a') as fp:
            print >>fp, message

    def create_template(self):

        # take given input file and create a template file with an injected CSS
        # file for the flowables and an empty body (with placeholder for inserting
        # the flowable html snippets)

        with open(self.index_html, 'rb') as fp:

            root = lxml.html.fromstring(fp.read())

            head = root.find('head')
            link = lxml.html.Element('link')
            link.attrib.update(dict(rel='stylesheet', type='text/css', href='flowable.css'))
            head.append(link)

            body = root.find('body')
            body.text = u'{body}'
            for child in body.iterchildren():
                body.remove(child)

            template_fn = os.path.join(self.tmpdir, 'template.html')
            with open(template_fn, 'wb') as fp_out:
                fp_out.write(lxml.html.tostring(root, encoding=unicode))

            self._log('generated template: {}'.format(template_fn))

    def extract_flowables(self):
        """ Extract flowables into dedicated HTML snippet files and replace 
            them using a custom markup.
        """


        with open(self.index_html, 'rb') as fp:
            root = lxml.html.fromstring(fp.read())

        sel = CSSSelector('.floatable-next-page')

        for num, node in enumerate(sel(root)):

            float_fn = os.path.join(self.tmpdir, 'floatable-{}.html'.format(num+1))
            base_fn, ext  = os.path.splitext(float_fn)
            with open(float_fn, 'wb') as fp:
                fp.write(lxml.html.tostring(node))
                self._log('generated flowable: {}'.format(float_fn))

            floatable_id = 'floatable-{}'.format(num+1)
            outer_html = outer_tmpl.format(id=floatable_id)
            new_node = lxml.html.fromstring(outer_html)
            node.getparent().replace(node, new_node)

        with open(self.index2_html, 'wb') as fp:
            fp.write(lxml.html.tostring(root))
            
        self._log('generated html file: {}'.format(self.index2_html))

    def create_pdf(self, areatree=False):
        result = self.run_ah(
            self.index2_html,
            self.index2_pdf,
            areatree=areatree)
        self._log('generated PDF from {} (areatree={})'.format(self.index2_html, areatree))
        return result

    def run_ah(self, input_fn, pdf_fn, areatree=False):
        """ Run Antennahouse on given input file ``index.fn`` generating
            a PDF output file ``pdf_fn``.
        """

        if areatree:
            cmd = 'run.sh -p @AreaTree -d "{}" | xmllint --format - >"{}"'.format(input_fn, self.index2_areatree)
        else:
            cmd = 'run.sh -d "{}" -o "{}"'.format(input_fn, pdf_fn)

        self._log(cmd)
        status, output = commands.getstatusoutput(cmd)
        self._log(output)
        if status != 0:
            raise RuntimeError('{} executed with status {}'.format(cmd, status))

    def process_floatables(self):


        with open(self.index2_areatree, 'rb') as fp:
            root = lxml.etree.fromstring(fp.read())

        result = dict()
        for node in root.xpath('//*[contains(@text,"id=")]'):
            current = node
            while current.tag != '{http://www.antennahouse.com/names/XSL/AreaTree}PageViewportArea':
                current = current.getparent()

            page_no = int(current.attrib['page-number'])
            abs_page_no = int(current.attrib['abs-page-number'])
            text = node.attrib['text']
            
            d = dict(
                    text=text,
                    page_no=page_no,
                    abs_page_no=abs_page_no)
            for item in text.split('::'):
                k, v = item.split('=')
                d[k] = v
            result[abs_page_no] = d

        self._log(pprint.pformat(result))

        with open(self.index2_pdf, 'rb') as fp_in:
            reader = PyPDF2.PdfFileReader(fp_in)
            writer = PyPDF2.PdfFileWriter()

            for page_no in range(reader.numPages):
                page_data = result.get(page_no + 1)
                page = reader.getPage(page_no)
                if page_data:
                    floatable_id = page_data['id']
                    floatable_html_fn = os.path.join(self.tmpdir, '{}.html'.format(floatable_id))
                    floatable_html_fn2 = os.path.join(self.tmpdir, '{}-2.html'.format(floatable_id))
                    # wrap floatable HTML snippet with template.html
                    with open(os.path.join(self.tmpdir, 'template.html'), 'rb') as template_in:
                        with open(floatable_html_fn, 'rb') as floatable_html_in:
                            template_html = template_in.read()
                            template_html = template_html.format(body=floatable_html_in.read())
                            with open(floatable_html_fn2, 'wb') as floatable_html_out:
                                floatable_html_out.write(template_html)

                    floatable_pdf_fn = os.path.join(self.tmpdir, '{}.pdf'.format(floatable_id))
                    self.run_ah(floatable_html_fn, floatable_pdf_fn)
                    with open(floatable_pdf_fn, 'rb') as floatable_in:
                        print '*'*80
                        print 'merging', floatable_pdf_fn
                        floatable_reader = PyPDF2.PdfFileReader(floatable_in)
                        page.mergePage(floatable_reader.getPage(0))

                writer.addPage(page)

            with open(self.pdf_final, 'wb') as fp_out:
                writer.write(fp_out)
                print 'resulting PDF: {}'.format(self.pdf_final)

    def __str__(self):
        return '{}(logfile={}, workdir={})'.format(self.__class__.__name__, self.logfile, self.tmpdir)

    def __call__(self):
        self.create_template()
        self.extract_flowables()
        self.create_pdf()
        self.create_pdf(areatree=True)
        self.process_floatables()

if __name__ == '__main__':
    proc = Processor('index.html')
    proc()
