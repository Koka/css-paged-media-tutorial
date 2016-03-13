
import os
import lxml.html

html_dir = 'build/html'

for name in os.listdir(html_dir):
    fname = os.path.join(html_dir, name)
    if not os.path.isfile(fname):
        continue
    with open(fname, 'rb') as fp:
        root = lxml.html.fromstring(fp.read())

    nodes = root.xpath('//title')
    if nodes:
        title = nodes[0].text
        title += u' - CSS Paged Media Tutorial and Showcase - Andreas Jung, ZOPYX'
        nodes[0].title = title
        print 'changed'
        print fname
    html = lxml.html.tostring(root)
    with open(fname, 'wb') as fp:
        fp.write(html.encode('utf8'))
