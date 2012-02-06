# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

xoj2pdf.jar: manifest.txt XournalToPDF.class
	jar -cfm $@ $^

%.class: %.java
	javac $^

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.orig
