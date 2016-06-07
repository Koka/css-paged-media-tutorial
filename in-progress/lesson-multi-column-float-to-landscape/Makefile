AH_OPTIONS=-2pass -lpdf -tpdf

all:
	bin/python process.py index.html
	run.sh $(AH_OPTIONS) -d index-out.html >index-out.pdf
	run.sh $(AH_OPTIONS) -p @AreaTree -d index-out.html | xmllint --format - >index-out.parsetree
	bin/python parse_parsetree.py index-out.parsetree
