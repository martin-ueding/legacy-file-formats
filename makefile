# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py)

###############################################################################
#                               Public Targets                                #
###############################################################################

all: legacy.1 legacy.1.html

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) legacy.1
	$(RM) legacy.1.html
	$(RM) legacyc

epydoc: html/index.html

install:
	install legacy $(DESTDIR)/usr/bin/
	install export/nb2pdf $(DESTDIR)/usr/bin/
	install export/xcf2png $(DESTDIR)/usr/bin/
	install --mode=644 legacylib $(DESTDIR)/usr/local/lib/python2.7/site-packages/

###############################################################################
#                               Private Targets                               #
###############################################################################

legacy.1: legacy.1.markdown
	pandoc -s $< -o $@

legacy.1.html: legacy.1.markdown
	pandoc -s -5 $< -o $@

html/index.html: legacy $(pythonfiles)
	epydoc -v $^
