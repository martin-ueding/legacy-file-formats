#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
Library for the legacy script.

Contains functions to check folders, rename found files.
"""

import os
import subprocess

import file_formats
import table

_patterns = file_formats.get_patterns()

_pattern_makefile = os.path.expanduser("~/.config/legacy/patterns.makefile")

def checkfolder(args, dirname, names):
    """
    Checks a folder for files that lack an export.

    @param args: Arguments passed from C{os.walk}.
    @type args: list
    @param dirname: Name of the currently parsed directory.
    @type dirname: str
    @param names: List of files and directories in the folder.
    @type names: list
    """
    options, counts = args

    names.sort()

    # Iterate thorugh all the files and folders.
    for name in names:
        nameparts = name.lower().split('.')

        # A folder `pages` should not be picked up, a folder `.bzr` should be.
        if len(nameparts) == 1:
            continue

        suffix = nameparts[-1]
        if suffix in _patterns:
            _check_file(name, options, counts, dirname, suffix)


def _check_file(name, options, counts, dirname, pattern):
    """
    Checks a file for export file(s).

    In case C{file.old} does not have a C{file.old.pdf}, a C{file.pdf} is checked
    alternatively. It the latter is found, it is moved to C{file.old.pdf} to
    show that it is just an export of the original file, not a file on its own.

    @param name: Name of the file.
    @type name: str
    @param dirname: Directory of the file.
    @type dirname: str
    @param options: Program options.
    @type options: object
    @param counts: Suffix statistics.
    @type counts: dict
    @param pattern: Suffix of this file.
    @type pattern: str
    """
    is_invalid = True

    # Check whether a file exist with one of the allowed suffixes.
    if "export_suffixes" in _patterns[pattern]:
        for exportsuffix in _patterns[pattern]["export_suffixes"]:
            # This is the standard export file name.
            exportfile = dirname+"/"+name+"."+exportsuffix

            _check_rename(dirname, name, exportfile, exportsuffix, options)

            # Check for the file again. This time, see whether its modification
            # time is newer than the original, if that option is specified.
            if os.path.isfile(exportfile):
                if options.time:
                    if _check_time(dirname+"/"+name, exportfile):
                        is_invalid = False
                else:
                    is_invalid = False

            if is_invalid and options.make:
                make_export(exportfile, options)

                # Check whether the file was successfully created now.
                if os.path.isfile(exportfile) and _check_time(dirname+"/"+name, exportfile):
                    is_invalid = False


    if is_invalid:
        _mark_invalid(dirname, name, pattern, counts)


def make_export(exportfile, options):
    """
    Uses a central makefile to create the export file.

    @param exportfile: File to be exported.
    @type exportfile: str
    @return: Whether C{make} returned with success.
    @rtype: bool
    """
    if not os.path.isfile(_pattern_makefile):
        print "Please create a pattern makefile at"
        print _pattern_makefile
        sys.exit(1)

    try:
        output = subprocess.check_output(["make", "-f", _pattern_makefile, "-C", os.path.dirname(exportfile), exportfile], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False
    else:
        if options.verbose:
            print output

        return True


def _check_time(origfile, exportfile):
    """
    Check whether C{origfile} is older than C{exportfile}.

    @param origfile: Path to first file.
    @type origfile: str
    @param exportfile: Path to second file.
    @type exportfile: str
    @return: Whether first file is older than second.
    @rtype: bool
    """
    origtime = os.path.getmtime(origfile)
    exporttime = os.path.getmtime(exportfile)

    # If the export is newer than the origtime, the
    # file is valid.
    valid = exporttime >= origtime

    return valid


def _check_rename(dirname, name, exportfile, exportsuffix, options):
    """
    Check whether the file has the same name, but just a export extension.

    Rename the file then.

    @param dirname: Directory of the original file.
    @param name: Name of the original file.
    @param exportfile: Expected exportfile.
    @param exportsuffix: Expected suffix of the export file.
    @param options: General program options.
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

    @param dirname: Directory of the file.
    @param name: Name of the file.
    @param pattern: Suffix of the original file.
    @param counts: Dict with suffix counts.
    """
    print os.path.normpath(dirname+"/"+name)

    if not pattern in counts:
        counts[pattern] = 0

    counts[pattern] += 1


def print_summary(counts):
    """
    Prints a statistic.

    @param counts: Dict with C{suffix: counts} pairs.
    """
    if len(counts) == 0:
        return

    print

    table.print_table(
        ["Count", "Suffix", "Name"],
        [[str(counts[key]).rjust(5), key, _patterns[key]["name"]] for key in sorted(counts)]
    )


def show_formats():
    """
    Prints a table of all supported formats.
    """
    table_data = []
    for pattern in sorted(_patterns):
        cur_pattern = _patterns[pattern]
        table_row = []

        table_row.append(pattern)

        if "name" in cur_pattern:
            table_row.append(cur_pattern["name"])
        else:
            table_row.append("")

        if "export_suffixes" in cur_pattern:
            table_row.append(', '.join(sorted(cur_pattern["export_suffixes"])))
        else:
            table_row.append("")

        table_data.append(table_row)

    proc = subprocess.Popen(["less", "-FRSX"], stdin=subprocess.PIPE)
    table.print_table(
        ["Suffix", "Name", "Export Suffixes"],
        table_data,
        outfile = proc.stdin
    )
    proc.stdin.close()
    proc.communicate()
