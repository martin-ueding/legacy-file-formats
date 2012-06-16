# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                   License                                   #
###############################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

pythonfiles:=$(wildcard *.py */*.py)

###############################################################################
#                               Public Targets                                #
###############################################################################

all: legacy.1
	make -C export

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) legacy.1
	$(RM) legacyc
	make -C export clean

epydoc: html/index.html

install:
	install export/nb2pdf $(DESTDIR)/usr/bin/
	install export/xcf2png $(DESTDIR)/usr/bin/
	install export/xoj2pdf/xoj2pdf $(DESTDIR)/usr/bin/
	install -d $(DESTDIR)/etc/legacy
	install --mode=664 export/patterns.makefile $(DESTDIR)/etc/legacy/
	mkdir -p /usr/share/man/man1/
	gzip -c legacy.1 > $(DESTDIR)/usr/share/man/man1/legacy.1.gz
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

html/index.html: legacy $(filter-out setup.py,$(pythonfiles))
	epydoc -v $^

legacy.1: legacy.1.rst
	rst2man $< $@
