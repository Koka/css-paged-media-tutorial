AH_OPTIONS=-2pass -lpdf -tpdf

all:
	bin/python process.py index.html
	run.sh $(AH_OPTIONS) -d index-out.html >index-out.pdf
	bin/python parse_pdf.py index-out.pdf
