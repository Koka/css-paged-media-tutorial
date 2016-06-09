import os
import sys
import lxml.html
import ah
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

fn = sys.argv[-1]



    # take given input file and create a template file with an injected CSS
    # file for the flowables and an empty body (with placeholder for inserting
    # the flowable html snippets)

    with open(fn, 'rb') as fp:

        root = lxml.html.fromstring(fp.read())

        head = root.find('head')
        link = lxml.html.Element('link')
        link.attrib.update(dict(rel='stylesheet', type='text/css', href='flowable.css'))
        head.append(link)

        body = root.find('body')
        body.text = u'{body}'
        for child in body.iterchildren():
            body.remove(child)

        template_fn = os.path.join(os.path.dirname(fn), template_fn)
        with open(template_fn, 'wb') as fp_out:
            fp_out.write(lxml.html.tostring(root, encoding=unicode))

        print 'template generated: {}'.format(template_fn)

def extract_flowables(fn, output_fn='index-out.html'):
    """ Extract flowables into dedicated HTML snippet files and replace 
        them using a custom markup.
    """


    with open(fn, 'rb') as fp:
        root = lxml.html.fromstring(fp.read())

    dirname = os.path.dirname(fn)
    sel = CSSSelector('.floatable-next-page')

    for num, node in enumerate(sel(root)):

        float_fn = os.path.join(dirname, 'floatable-{}.html'.format(num+1))
        base_fn, ext  = os.path.splitext(float_fn)
        with open(float_fn, 'wb') as fp:
            fp.write(lxml.html.tostring(node))
            print 'generated flowable: {}'.format(float_fn)

        floatable_id = 'floatable-{}'.format(num+1)
        outer_html = outer_tmpl.format(id=floatable_id)
        new_node = lxml.html.fromstring(outer_html)
        node.getparent().replace(node, new_node)

    output_fn = os.path.join(dirname, output_fn)
    with open(output_fn, 'wb') as fp:
        fp.write(lxml.html.tostring(root))
        
    print 'Output written to', output_fn
    return output_fn


def create_pdf(fn, pdf_out_fn='index-out.pdf', areatree=False):
    return ah.run_ah(fn, pdf_out_fn, areatree=areatree)


if __name__ == '__main__':

    fn = os.path.abspath(sys.argv[-1])
    print 'processing: {}'. format(fn)
    create_template(fn)
    fn2 = extract_flowables(fn)
    create_pdf(fn2)
    create_pdf(fn2, areatree=True)
