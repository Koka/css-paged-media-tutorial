import os
import sys
import lxml.html
from lxml.cssselect import CSSSelector


outer_tmpl = """
<div class="outer floatable" data-float-fn="{float_fn}" id="{id}">
    <div class="inner">
        <div class="wrapper">
        template={template}
        </div>
    </div>
</div>
"""

fn = sys.argv[-1]
with open(fn, 'rb') as fp:
    root = lxml.html.fromstring(fp.read())

sel = CSSSelector('.floatable-next-page')

for num, node in enumerate(sel(root)):

    float_fn = 'floatable-{}.html'.format(num+1)
    base_fn, ext  = os.path.splitext(float_fn)
    with open(float_fn, 'wb') as fp:
        fp.write(lxml.html.tostring(node))
    cmd = 'run.sh -d "{base_fn}.html" -o "{base_fn}.pdf"'.format(base_fn=base_fn)
    print cmd
    os.system(cmd)

    id = 'floatable-{}'.format(num+1)
    outer_html = outer_tmpl.format(float_fn=float_fn, template=float_fn, id=id)
    new_node = lxml.html.fromstring(outer_html)
    node.getparent().replace(node, new_node)

base, ext = os.path.splitext(fn)
out_fn = '{}-out{}'.format(base, ext)
with open(out_fn, 'wb') as fp:
    fp.write(lxml.html.tostring(root))
print 'Output written to', out_fn
