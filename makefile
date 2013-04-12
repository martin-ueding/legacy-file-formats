# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py */*.py)

###############################################################################
#                               Public Targets                                #
###############################################################################

all: legacy.1
	make -C export

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r build
	$(RM) -r dist
	$(RM) -r html
	$(RM) legacy.1
	$(RM) legacyc
	make -C export clean

epydoc: html/index.html

install:
	install -d "$(DESTDIR)/usr/share/man/man1/"
	gzip -c legacy.1 > "$(DESTDIR)/usr/share/man/man1/legacy.1.gz"
#
	install -d "$(DESTDIR)/usr/share/legacy"
	install --mode=644 "export/xoj2pdf/xoj2pdf.jar" "$(DESTDIR)/usr/share/legacy/"
#
	install -d "$(DESTDIR)/etc/legacy"
	install --mode=644 "formats.yaml" "$(DESTDIR)/etc/legacy/"
	install --mode=664 "export/patterns.makefile" "$(DESTDIR)/etc/legacy/"
#
	install -d "$(DESTDIR)/usr/bin/"
	install "export/nb2pdf" "$(DESTDIR)/usr/bin/"
	install "export/xcf2png" "$(DESTDIR)/usr/bin/"
	install "export/xoj2pdf/xoj2pdf" "$(DESTDIR)/usr/bin/"
#
	python setup.py install --prefix "$(DESTDIR)"

uninstall:
	$(RM) "$(DESTDIR)/usr/bin/nb2pdf"
	$(RM) "$(DESTDIR)/usr/bin/xcf2png"
	$(RM) "$(DESTDIR)/usr/bin/xoj2pdf"
	$(RM) -rf "$(DESTDIR)/etc/legacy""
	$(RM) -rf "$(DESTDIR)/usr/share/legacy/"
	$(RM) "/usr/share/man/man1/legacy.1.gz"

###############################################################################
#                               Private Targets                               #
###############################################################################

html/index.html: legacy $(filter-out setup.py,$(pythonfiles))
	epydoc -v $^

legacy.1: legacy.1.rst
	rst2man $< $@
