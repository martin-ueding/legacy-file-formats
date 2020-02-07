# Copyright © 2012-2013 Martin Ueding <martin-ueding.de>

xoj2pdf.jar: manifest.txt XournalToPDF.class
	jar -cfm $@ $^

%.class: %.java
	javac -encoding UTF-8 $^

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.orig
