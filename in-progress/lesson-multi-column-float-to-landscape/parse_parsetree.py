import os
import re
import sys
import tempfile
import commands
import lxml.etree


in_fn = sys.argv[-1]
with open(in_fn, 'rb') as fp:
    root = lxml.etree.fromstring(fp.read())

result = list()
for node in root.xpath('//*[contains(@text,"template::")]'):
    current = node
    while current.tag != '{http://www.antennahouse.com/names/XSL/AreaTree}PageViewportArea':
        current = current.getparent()

    page_no = current.attrib['page-number']
    abs_page_no = current.attrib['abs-page-number']
    text = node.attrib['text']
    result.append(dict(
            text=text,
            page_no=page_no,
            abs_page_no=abs_page_no))

print result

