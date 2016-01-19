all: pdfreactor prince antennahouse vivliostyle

pdfreactor:
	pdfreactor -v -j index.html pdfreactor.pdf

prince: 
	prince -v --javascript index.html prince.pdf

vivliostyle: 
	vivliostyle-formatter index.html 

antennahouse:
	run.sh -d  index.html -o antennahouse.pdf

clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	git rm -r images
	rm -fr images
	mkdir -p images/pdfreactor images/prince images/antennahouse images/vivliostyle
	convert -density 150 -quality 75 pdfreactor.pdf         images/pdfreactor/pdfreactor.jpg
	convert -density 150 -quality 75 prince.pdf             images/prince/prince.jpg
	convert -density 150 -quality 75 antennahouse.pdf       images/antennahouse/antennahouse.jpg
	convert -density 150 -quality 75 vivliostyle-output.pdf images/vivliostyle/vivliostyle.jpg
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
