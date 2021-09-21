.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  book        to build the book"
	@echo "  clean       to clean out site build files"
	@echo "  commit      to build the book and commit to gh-pages online"
	@echo "  pdf         to build the sites PDF"


book:
	python add_metadata.py
	python add_tag.py thebe-init
	jupyter-book build ./
	python thebe_mikaem.py
	#ghp-import -n -p -f _build/html

commit:
	jupyter-book build ./
	ghp-import -n -p -f _build/html

clean:
	jupyter-book clean ./

pdf:
	jupyter-book build ./ --builder pdflatex
