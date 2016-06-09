import os
import sys
import tempfile
import lxml.html
import shutil
import commands
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

    def __str__(self):
        return '{}(logfile={}, workdir={})'.format(self.__class__.__name__, self.logfile, self.tmpdir)

    def __call__(self):
        self.create_template()
        self.extract_flowables()
        self.create_pdf()
        self.create_pdf(areatree=True)


if __name__ == '__main__':
    proc = Processor('index.html')
    import pdb; pdb.set_trace() 
    print proc
    proc()
