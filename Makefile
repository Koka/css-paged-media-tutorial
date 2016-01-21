all: pdfreactor prince antennahouse vivliostyle

pdfreactor:
	-pdfreactor -v -j index.html pdfreactor.pdf

prince: 
	-prince -v --javascript index.html prince.pdf

vivliostyle: 
	-vivliostyle-formatter index.html 

antennahouse:
	-run.sh -d  index.html -o antennahouse.pdf

clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	mkdir -p images/pdfreactor images/princexml images/antennahouse images/vivliostyle
	echo placeholder >images/placeholder
	-convert -density 150 -quality 85 pdfreactor.pdf         images/pdfreactor/pdfreactor.png
	-convert -density 150 -quality 85 prince.pdf             images/princexml/prince.png
	-convert -density 150 -quality 85 antennahouse.pdf       images/antennahouse/antennahouse.png
	-convert -density 150 -quality 85 vivliostyle-output.pdf images/vivliostyle/vivliostyle.png
	git add images
	git commit -m updated images

git: clean all 
	git add *pdf
	git commit -m updated *pdf

push: 
	git push


docs: FORCE
	git pull
	virtualenv-2.7 .
	bin/pip install sphinx sphinx-bootstrap-theme ninja sphinxcontrib-googleanalytics
	cd docs; make html
	cp -av docs/build/html/* /var/www/print-css.rocks

FORCE:
