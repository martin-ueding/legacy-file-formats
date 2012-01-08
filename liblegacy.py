#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
Library for the legacy script.

Contains functions to check folders, rename found files.
"""

__docformat__ = "javadoc en"

import os

import file_formats
import table

_patterns = file_formats.get_patterns()

def checkfolder(args, dirname, names):
    """
    Checks a folder for files that lack an export.

    @param args Arguments passed from `os.walk`.
    @param dirname Name of the currently parsed directory.
    @param names List of files and directories in the folder.
    """
    options, counts = args

    names.sort()

    # Iterate thorugh all the files and folders.
    for name in names:
        for pattern in _patterns:
            if name.lower().endswith("."+pattern):
                _check_file(name, options, counts, dirname, pattern)


def _check_file(name, options, counts, dirname, pattern):
    """
    Checks a file for export file(s).

    In case `file.old` does not have a `file.old.pdf`, a `file.pdf` is checked
    alternatively. It the latter is found, it is moved to `file.old.pdf` to
    show that it is just an export of the original file, not a file on its own.

    @param name Name of the file.
    @param dirname Directory of the file.
    @param options Program options.
    @param counts Suffix statistics.
    @param pattern Suffix of this file.
    """
    is_invalid = True

    # Check whether a file exist with one of the allowed suffixes.
    for exportsuffix in _patterns[pattern][1]:
        # This is the standard export file name.
        exportfile = dirname+"/"+name+"."+exportsuffix

        _check_rename(dirname, name, exportfile, exportsuffix, options)

        # Check for the file again. This time, see whether its modification
        # time is newer than the original, if that option is specified.
        if os.path.isfile(exportfile):
            if options.time:
                if not _check_time(dirname+"/"+name, exportfile):
                    is_invalid = False
            else:
                is_invalid = False

    if is_invalid:
        _mark_invalid(dirname, name, pattern, counts)


def _check_time(origfile, exportfile):
    """
    Check whether `origfile` is older than `exportfile`.

    @param origfile Path to first file.
    @param exportfile Path to second file.
    @return Whether first file is older than second.
    """
    origtime = os.path.getmtime(origfile)
    exporttime = os.path.getmtime(exportfile)

    # If the export is newer than the origtime, the
    # file is valid.
    return exporttime > origtime


def _check_rename(dirname, name, exportfile, exportsuffix, options):
    """
    Check whether the file has the same name, but just a export extension.

    Rename the file then.

    @param dirname Directory of the original file.
    @param name Name of the original file.
    @param exportfile Expected exportfile.
    @param exportsuffix Expected suffix of the export file.
    @param options General program options.
    """
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


def _mark_invalid(dirname, name, pattern, counts):
    """
    Marks a file as having no export.

    @param dirname Directory of the file.
    @param name Name of the file.
    @param pattern Suffix of the original file.
    @param counts Dict with suffix counts.
    """
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
        [[str(counts[key]).rjust(5), key, _patterns[key][0]] for key in sorted(counts)]
    )


def show_formats():
    """
    Prints a table of all supported formats.
    """
    table.print_table(
        ["Suffix", "Name", "Export Suffixes"],
        [[pattern, _patterns[pattern][0], ', '.join(sorted(_patterns[pattern][1]))] for pattern in sorted(_patterns)]
    )
