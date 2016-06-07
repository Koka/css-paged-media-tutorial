import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader


overlay_pdf_file_name = 'overlay_PDF.pdf'
pdf_template_file_name = 'base_PDF_template.pdf'
result_pdf_file_name = 'final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = fpdf.FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = 'B'
pdf.set_font("Arial", style=pdf_style, size=10)
pdf.set_xy(100, 100)
pdf.cell(0, 10, txt='THIS IS THE TEXT THAT IS GOING IN YOUR FIELD', ln=0)
pdf.output(overlay_pdf_file_name)
pdf.close()

# Take the PDF you created above and overlay it on your template PDF
# Open your template PDF
pdf_template = PdfFileReader(file(pdf_template_file_name, 'rb'))
# Get the first page from the template
template_page = pdf_template.getPage(0)
# Open your overlay PDF that was created earlier
overlay_pdf = PdfFileReader(file(overlay_pdf_file_name, 'rb'))
# Merge the overlay page onto the template page
template_page.mergePage(overlay_pdf.getPage(0))
# Write the result to a new PDF file
output_pdf = PdfFileWriter()
output_pdf.addPage(template_page)
