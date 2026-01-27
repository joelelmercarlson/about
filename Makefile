UV_RUN  := uv run

HOMEDIR := $(HOME)
ABOUT   := $(HOME)/about
MDS     := $(wildcard $(ABOUT)/*.md)
MD_DOCS := architect consultant readme resume tools
MD_TO_HTML  := $(UV_RUN) markdown_to_html.py
WEB         := /var/www/html
HTML        := html
CSS         := $(wildcard $(HTML)/*.css)
HTML_DOCS   := $(wildcard $(HTML)/*.html)
README_HTML := $(HTML)/readme.html
INDEX_HTML  := $(WEB)/index.html


all: build 
.PHONY: all

install: 
	sudo cp -r $(HTML_DOCS) $(WEB)
	sudo cp -r $(CSS) $(WEB)
	sudo cp $(README_HTML) $(INDEX_HTML)

build:
	for f in $(MD_DOCS); do \
		echo "$$f"; \
		$(MD_TO_HTML) $$f.md $(HTML)/$$f.html; \
	done
