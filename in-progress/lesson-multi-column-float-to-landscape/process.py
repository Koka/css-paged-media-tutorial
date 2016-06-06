import os
import sys
import lxml.html
from lxml.cssselect import CSSSelector


outer_tmpl = """
<div class="outer" data-float-fn="{float_fn}">
    <div class="inner">
        <div class="wrapper">
        template::{template}::HELLO WORLD::ABC=DEF:XXX=EFD
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
    with open(float_fn, 'wb') as fp:
        fp.write(lxml.html.tostring(node))

    outer_html = outer_tmpl.format(float_fn=float_fn, template=float_fn)
    new_node = lxml.html.fromstring(outer_html)
    node.getparent().replace(node, new_node)

base, ext = os.path.splitext(fn)
out_fn = '{}-out{}'.format(base, ext)
with open(out_fn, 'wb') as fp:
    fp.write(lxml.html.tostring(root))
print 'Output written to', out_fn
