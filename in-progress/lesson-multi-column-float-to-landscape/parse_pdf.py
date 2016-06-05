import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


with open(sys.argv[-1], 'rb') as fp:
    pdf = PdfFileReader(fp)
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        print i
