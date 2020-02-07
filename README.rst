.. Copyright © 2012-2014, 2016-2017 Martin Ueding <martin-ueding.de>

legacy file formats
===================

When I had a Mac, I would use programs like Keynote, Pages and third party
software like Mindnode. Now I use GNU/Linux and do not have regular access to
those programs any more. Therefore, I need to convert them into PDF or the
likes.

Those files are all over my hard drive. Some of them already have a PDF
exported, some do not. In order to find those, that still need a PDF exported,
I wrote a Python script.

It searches through the current directory (or any folders you specify on the
command line) an searches for files that are not easy to open on GNU/Linux.

Say you have ``presentation.odp`` but want to have a corresponding PDF to it.
The script will check for a ``presentation.odp.pdf``. In case that is not
there, it will resort to ``presentation.pdf`` and rename it to
``presentation.odp.pdf`` to make clear that it is exported.

Finds files which might become unreadable.

installation
------------
::

    make
    sudo make install


uninstall
---------
::

    sudo make uninstall


usage
-----
See ``legacy -h`` or the manpage_.

.. _manpage: legacy.1.rst
