# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py */*.py)

###############################################################################
#                               Public Targets                                #
###############################################################################

all: legacy.1 legacy.1.html legacy.1.gz

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) legacy.1
	$(RM) legacy.1.html
	$(RM) legacyc

epydoc: html/index.html

install:
	install export/nb2pdf $(DESTDIR)/usr/bin/
	install export/xcf2png $(DESTDIR)/usr/bin/
	install --mode=644 legacy.1.gz /usr/share/man/man1/
	python setup.py install

uninstall:
	$(RM) $(DESTDIR)/usr/bin/nb2pdf
	$(RM) $(DESTDIR)/usr/bin/xcf2png
	$(RM) /usr/share/man/man1/legacy.1.gz

###############################################################################
#                               Private Targets                               #
###############################################################################

html/index.html: legacy $(pythonfiles)
	epydoc -v $^

legacy.1: legacy.1.markdown
	pandoc -s $< -o $@

legacy.1.gz: legacy.1
	cat $< | gzip > $@

legacy.1.html: legacy.1.markdown
	pandoc -s -5 $< -o $@
