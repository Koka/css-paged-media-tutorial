all: pdfreactor prince vivliostyle antennahouse

pdfreactor:
	pdfreactor -s styles.css index.xml pdfreactor.pdf

prince: 
	prince -s styles.css  index.xml prince.pdf

vivliostyle: 
	vivliostyle-formatter index.xml 

antennahouse: 
	run.sh -d index.xml -o antennahouse.pdf

clean:
	find . -name \*.pdf -exec rm {} \;

git: clean all 
	git add *pdf
	git commit -m updated *pdf

images: FORCE
	mkdir -p images/pdfreactor images/princexml images/antennahouse images/vivliostyle
	echo placeholder >images/placeholder
	convert -density 150 -quality 75 pdfreactor.pdf         images/pdfreactor/pdfreactor.jpg
	convert -density 150 -quality 75 prince.pdf             images/princexml/prince.jpg
	convert -density 150 -quality 75 antennahouse.pdf       images/antennahouse/antennahouse.jpg
	convert -density 150 -quality 75 vivliostyle-output.pdf images/vivliostyle/vivliostyle.jpg
	git add images
	git commit -m updated images

FORCE:
