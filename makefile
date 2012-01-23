# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py)

all: epydoc legacy.1 legacy.1.html

legacy.1: legacy.1.markdown
	pandoc -s $< -o $@

legacy.1.html: legacy.1.markdown
	pandoc -s -5 $< -o $@
	
epydoc: html/index.html

html/index.html: legacy $(pythonfiles)
	epydoc $^

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
