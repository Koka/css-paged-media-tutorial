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
	convert -density 150 -quality 85 pdfreactor.pdf         images/pdfreactor/pdfreactor.png
	convert -density 150 -quality 85 prince.pdf             images/princexml/prince.png
	convert -density 150 -quality 85 antennahouse.pdf       images/antennahouse/antennahouse.png
	convert -density 150 -quality 85 vivliostyle-output.pdf images/vivliostyle/vivliostyle.png
	git add images
	git commit -m updated images

FORCE:
