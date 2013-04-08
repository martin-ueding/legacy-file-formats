# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

xoj2pdf.jar: manifest.txt XournalToPDF.class
	jar -cfm $@ $^

%.class: %.java
	javac $^

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.orig
