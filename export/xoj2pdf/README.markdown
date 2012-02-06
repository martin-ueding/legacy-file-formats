This is a very hacky program, since it uses the user interface of Xournal.
This is meant as a temporary fix until Xournal comes with a command line option
to export to PDF.

It will take some "file.xoj" and save it to "file.xoj.pdf" in the same folder
that the original file was in. This is how Xournal handles its export.

Xournal might crash, do something unknown in between. This program has no way
of checking the status of the Xournal instance, so you might get a mess.
