# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

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
