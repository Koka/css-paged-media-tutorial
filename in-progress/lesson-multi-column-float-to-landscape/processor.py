import os
import sys
import tempfile
import lxml.html
import shutil
import pprint
import subprocess
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

    def __init__(self, 
        input_directory='src', 
        input_filename='index.html', 
        output_directory=None, 
        styles_directory='styles',
        ah_options=''):
        self.input_directory = input_directory
        self.input_filename = input_filename
        self.input_filename = os.path.abspath(os.path.join(self.input_directory, self.input_filename))
        self.ah_options = ah_options
        self.styles_directory = styles_directory
        if output_directory:
            if os.path.exists(output_directory):
                shutil.rmtree(output_directory)
            os.makedirs(output_directory)
            self.tmpdir = output_directory
        else:
            self.tmpdir = tempfile.mkdtemp()
        self.logfile = os.path.join(self.tmpdir, 'conversion.log')
        self.index_html = os.path.join(self.tmpdir, input_filename)
        self.index2_html = os.path.join(self.tmpdir, 'index2.html')
        self.index2_pdf= os.path.join(self.tmpdir, 'index2.pdf')
        self.index2_areatree = os.path.join(self.tmpdir, 'index2.areatree')
        self.pdf_final = os.path.join(self.tmpdir, 'final.pdf')
        self._copy_src()
        self._copy_resources()
        self._log('copied {} -> {}'.format(self.input_filename, self.index_html))

    def _recursive_copy(self, src, dst, ignore_top_level_dir=False):

        src = os.path.abspath(src)
        dst = os.path.abspath(dst)
        shutil.copytree(src, dst)

    def _copy_src(self):
        self._recursive_copy(self.input_directory, os.path.join(self.tmpdir, self.input_directory))

    def _copy_resources(self):
        self._recursive_copy(self.styles_directory, os.path.join(self.tmpdir, self.styles_directory))

    def _log(self, message, level='info'):
        with open(self.logfile, 'a') as fp:
            print(message, file=fp, sep='\n')

    def _runcmd(self, cmd):
        self._log('*' * 80)
        self._log(cmd)
        status, output = subprocess.getstatusoutput(cmd)
        self._log('Status: {}'.format(status))
        if output:
            self._log('Output:\n{}'.format(output))
        if status != 0:
            raise RuntimeError('Execution of "{}" failed\n\nOutput:\n{}'.format(cmd, output))

    def get_log(self):
        with open (self.logfile, 'r') as fp:
            return fp.read()

    def create_template(self):

        # take given input file and create a template file with an injected CSS
        # file for the flowables and an empty body (with placeholder for inserting
        # the flowable html snippets)

        with open(self.index_html, 'rb') as fp:

            root = lxml.html.fromstring(fp.read())

            head = root.find('head')
            link = lxml.html.Element('link')
            link.attrib.update(dict(rel='stylesheet', type='text/css', href='styles/flowable.css'))
            head.append(link)

            body = root.find('body')
            body.text = u'{body}'
            for child in body.iterchildren():
                body.remove(child)

            template_fn = os.path.join(self.tmpdir, 'template.html')
            with open(template_fn, 'w') as fp_out:
                fp_out.write(lxml.html.tostring(root, encoding='unicode'))

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
            with open(float_fn, 'w') as fp:
                fp.write(lxml.html.tostring(node, encoding='unicode'))
                self._log('generated flowable: {}'.format(float_fn))

            floatable_id = 'floatable-{}'.format(num+1)
            outer_html = outer_tmpl.format(id=floatable_id)
            new_node = lxml.html.fromstring(outer_html)
            node.getparent().replace(node, new_node)

        with open(self.index2_html, 'w') as fp:
            fp.write(lxml.html.tostring(root, encoding='unicode'))
            
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
            cmd = 'run.sh {} -p @AreaTree -d "{}" | xmllint --format - >"{}"'.format(self.ah_options, input_fn, self.index2_areatree)
        else:
            cmd = 'run.sh {} -d "{}" -o "{}"'.format(self.ah_options, input_fn, pdf_fn)

        self._runcmd(cmd)

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

            for page_no in range(reader.numPages):
                page_data = result.get(page_no + 1)
                page = reader.getPage(page_no)

                pdf_out_fn = os.path.join(self.tmpdir, '{}.pdf').format(page_no + 1)
                writer = PyPDF2.PdfFileWriter()
                writer.addPage(page)
                with open(pdf_out_fn, 'wb') as pdf_out:
                    writer.write(pdf_out)

                if page_data:
                    floatable_id = page_data['id']
                    floatable_html_fn = os.path.join(self.tmpdir, '{}.html'.format(floatable_id))
                    floatable_html_fn2 = os.path.join(self.tmpdir, '{}-2.html'.format(floatable_id))
                    # wrap floatable HTML snippet with template.html
                    with open(os.path.join(self.tmpdir, 'template.html'), 'r') as template_in:
                        with open(floatable_html_fn, 'r') as floatable_html_in:
                            template_html = template_in.read()
                            template_html = template_html.format(body=floatable_html_in.read())
                            with open(floatable_html_fn2, 'w') as floatable_html_out:
                                floatable_html_out.write(template_html)

                    floatable_pdf_fn = os.path.join(self.tmpdir, 'floatable-{}.pdf'.format(page_no + 1))
                    self.run_ah(floatable_html_fn2, floatable_pdf_fn)

                    # merge with original PDF page
                    pdf_tmp_fn = tempfile.mktemp(suffix='.pdf')
                    cmd = 'pdftk "{}" background "{}" output "{}"'.format(pdf_out_fn, floatable_pdf_fn, pdf_tmp_fn)
                    self._runcmd(cmd)
                    shutil.copy(pdf_tmp_fn, pdf_out_fn)
                    os.unlink(pdf_tmp_fn)


            all_pdfs = ' '.join(['"{}"'.format(os.path.join(self.tmpdir, '{}.pdf').format(page_no + 1)) for page_no in range(reader.numPages)])
            cmd = 'pdftk {} cat output "{}"'.format(all_pdfs, self.pdf_final)
            self._runcmd(cmd)
            self._log('resulting PDF: {}'.format(self.pdf_final))

    def __str__(self):
        return '{}(logfile={}, workdir={})'.format(self.__class__.__name__, self.logfile, self.tmpdir)

    def __call__(self):
        self.create_template()
        self.extract_flowables()
        self.create_pdf()
        self.create_pdf(areatree=True)
        self.process_floatables()


if __name__ == '__main__':
    proc = Processor(
            input_directory='src',
            input_filename='src/index.html',
            styles_directory='styles',
            output_directory='/tmp/out',
            ah_options='-tpdf',
            )
    proc()
    print(proc.get_log())
