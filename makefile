# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py)

all: legacy.1 legacy.1.html

legacy.1: legacy.1.markdown
	pandoc -s $< -o $@

legacy.1.html: legacy.1.markdown
	pandoc -s -5 $< -o $@
	
epydoc: html/index.html

html/index.html: legacy $(pythonfiles)
	epydoc -v $^

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) legacy.1
	$(RM) legacy.1.html
	$(RM) legacyc
