# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

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

###############################################################################
#                              Office Documents                               #
###############################################################################

%.ods.pdf: %.ods
	libreoffice -convert-to pdf $< --headless
	mv $(<:.ods=.pdf) $@

%.odt.pdf: %.odt
	libreoffice -convert-to pdf $< --headless
	mv $(<:.odt=.pdf) $@

%.odg.pdf: %.odg
	libreoffice -convert-to pdf $< --headless
	mv $(<:.odg=.pdf) $@

%.odp.pdf: %.odp
	libreoffice -convert-to pdf $< --headless
	mv $(<:.odp=.pdf) $@

%.doc.pdf: %.doc
	libreoffice -convert-to pdf $< --headless
	mv $(<:.doc=.pdf) $@

%.docx.pdf: %.docx
	libreoffice -convert-to pdf $< --headless
	mv $(<:.docx=.pdf) $@

%.dotx.pdf: %.dotx
	libreoffice -convert-to pdf $< --headless
	mv $(<:.dotx=.pdf) $@

%.xls.pdf: %.xls
	libreoffice -convert-to pdf $< --headless
	mv $(<:.xls=.pdf) $@

%.xlsx.pdf: %.xlsx
	libreoffice -convert-to pdf $< --headless
	mv $(<:.xlsx=.pdf) $@

%.ppt.pdf: %.ppt
	libreoffice -convert-to pdf $< --headless
	mv $(<:.ppt=.pdf) $@

%.pptx.pdf: %.pptx
	libreoffice -convert-to pdf $< --headless
	mv $(<:.pptx=.pdf) $@

###############################################################################
#                            Mathematica Notebook                             #
###############################################################################

%.nb.pdf: %.nb
	cd $$(dirname $<) && nb2pdf

###############################################################################
#                              Xournal Notebook                               #
###############################################################################

%.xoj.pdf: %.xoj
	xoj2pdf $^
