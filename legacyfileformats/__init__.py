#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2014 Martin Ueding <dev@martin-ueding.de>

"""
This script searches your files for file formats that might be unreadable in
the future. It will check whether there is a corresponding PDF exported, if
not, the file will be listed.

For some file types, it can automatically generate an export file. You can
specify your own file formats as well as how they can be exported.
"""

import argparse
import os
import sys

from . import liblegacy

__docformat__ = "restructuredtext en"

def _parse_args():
    """
    Parses command line arguments.

    :return: Tuple with options and arguments.
    :rtype: tuple
    """
    parser = argparse.ArgumentParser(description="Checks for proprietary, rare or legacy file formats that do not have a PDF (or similarly standard) exported.")
    parser.add_argument("paths", nargs='*', help="Show known formats and exit.")
    parser.add_argument("--formats", dest="formats", action="store_true", default=False, help="Show known formats and exit.")
    parser.add_argument("--make", dest="make", action="store_true", default=False, help="Uses makefile to generate export files.")
    parser.add_argument("--rename", dest="rename", action="store_true", default=False, help="Rename file.pdf to file.old.pdf [default %(default)s].")
    parser.add_argument("--stat", dest="stat", action="store_true", default=False, help="Print file type summary. [default %(default)s]")
    parser.add_argument("--time", dest="time", action="store_true", default=False, help="Check that export is newer than other file. [default %(default)s]")
    parser.add_argument("-v", dest="verbose", action="store_true", default=False, help="Show renames (or would be renames). [default %(default)s].")

    return parser.parse_args()

def main():
    options = _parse_args()

    if options.formats:
        liblegacy.show_formats()
        sys.exit(1)

    # If no directory was given on the command line, use the current working
    # directory.
    if len(options.paths) == 0:
        options.paths.append(".")

    counts = {}

    # Iterate through all given folders.
    for path in options.paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                allnames = filenames + dirnames
                liblegacy.checkfolder(dirpath, allnames, options, counts)

    # Print the summary if desired.
    if options.stat:
        liblegacy.print_summary(counts)

if __name__ == "__main__":
    main()
