import os
import pprint
import sys
import lxml.etree
import PyPDF2


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

pprint.pprint(result)


pdf_in = 'index-out.pdf'
pdf_out = 'index-out2.pdf'

with open(pdf_in, 'rb') as fp_in:
    reader = PyPDF2.PdfFileReader(fp_in)
    writer = PyPDF2.PdfFileWriter()


    for page_no in range(reader.numPages):
        page = reader.getPage(page_no)
        writer.addPage(page)

    with open(pdf_out, 'wb') as fp_out:
        writer.write(fp_out)
