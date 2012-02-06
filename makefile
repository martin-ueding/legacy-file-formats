# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py */*.py)

###############################################################################
#                               Public Targets                                #
###############################################################################

all: legacy.1 legacy.1.html legacy.1.gz
	make -C export

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) legacy.1
	$(RM) legacy.1.html
	$(RM) legacyc
	make -C export clean

epydoc: html/index.html

install:
	install export/nb2pdf $(DESTDIR)/usr/bin/
	install export/xcf2png $(DESTDIR)/usr/bin/
	install export/xoj2pdf/xoj2pdf $(DESTDIR)/usr/bin/
	install -d $(DESTDIR)/etc/legacy
	install --mode=664 export/patterns.makefile $(DESTDIR)/etc/legacy/
	install --mode=644 legacy.1.gz /usr/share/man/man1/
	install --mode=644 formats.yaml $(DESTDIR)/etc/legacy/
	install -d $(DESTDIR)/usr/share/legacy
	install --mode=644 export/xoj2pdf/xoj2pdf.jar $(DESTDIR)/usr/share/legacy/
	python setup.py install

uninstall:
	$(RM) $(DESTDIR)/usr/bin/nb2pdf
	$(RM) $(DESTDIR)/usr/bin/xcf2png
	$(RM) $(DESTDIR)/usr/bin/xoj2pdf
	$(RM) -rf $(DESTDIR)/etc/legacy
	$(RM) -rf $(DESTDIR)/usr/share/legacy/
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
