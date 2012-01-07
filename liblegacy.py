#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

__docformat__ = "javadoc en"

from file_formats import patterns
import table

def checkfolder(args, dirname, names):
    """
    Checks a folder for files that lack an export.

    In case `file.old` does not have a `file.old.pdf`, a `file.pdf` is checked
    alternatively. It the latter is found, it is moved to `file.old.pdf` to
    show that it is just an export of the original file, not a file on its own.

    @param args Arguments passed from `os.walk`.
    @param dirname Name of the currently parsed directory.
    @param names List of files and directories in the folder.
    """
    options, counts = args

    names.sort()

    # Iterate thorugh all the files and folders.
    for name in names:
        for pattern in patterns:
            if name.lower().endswith("."+pattern):
                is_invalid = True

                # Check whether a file exist with one of the allowed suffixes.
                for exportsuffix in patterns[pattern][1]:
                    # This is the standard export file name.
                    exportfile = dirname+"/"+name+"."+exportsuffix

                    # Check whether the file has the same name, but just a
                    # export extension.  Rename the file then.
                    if not os.path.isfile(exportfile):
                        alt_exportfile = dirname+"/"+os.path.splitext(name)[0]+"."+exportsuffix
                        if os.path.isfile(alt_exportfile):
                            if options.rename:
                                os.rename(alt_exportfile, exportfile)
                                if options.verbose:
                                    print "Renaming", alt_exportfile, exportfile

                            else:
                                if options.verbose:
                                    print "Would rename", alt_exportfile, exportfile

                    # Check for the file again. This time, see whether its
                    # modification time is newer than the original, if that
                    # option is specified.
                    if os.path.isfile(exportfile):
                        if options.time:
                            origtime = os.path.getmtime(dirname+"/"+name)
                            exporttime = os.path.getmtime(exportfile)

                            # If the export is newer than the origtime, the
                            # file is valid.
                            if exporttime > origtime:
                                is_invalid = False
                        else:
                            is_invalid = False

                if is_invalid:
                    print dirname+"/"+name

                    if not pattern in counts:
                        counts[pattern] = 0

                    counts[pattern] += 1


def print_summary(counts):
    """
    Prints a statistic.

    @param counts Dict with `suffix: counts` pairs.
    """
    if len(counts) == 0:
        return

    print

    table.print_table(
        ["Count", "Suffix", "Name"],
        [[str(counts[key]).rjust(5), key, patterns[key][0]] for key in sorted(counts)]
    )


def show_formats():
    """
    Prints a table of all supported formats.
    """
    table.print_table(
        ["Suffix", "Name", "Export Suffixes"],
        [[pattern, patterns[pattern][0], ', '.join(sorted(patterns[pattern][1]))] for pattern in sorted(patterns)]
    )
