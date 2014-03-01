#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2014 Martin Ueding <dev@martin-ueding.de>

"""
Library for the legacy script.

Contains functions to check folders, rename found files.
"""

import os
import prettytable
import subprocess
import logging

from . import file_formats

__docformat__ = "restructuredtext en"

_patterns = file_formats.get_patterns()

def checkfolder(dirname, names, options, counts):
    """
    Checks a folder for files that lack an export.

    :param args: Arguments passed from C{os.walk}.
    :type args: list
    :param dirname: Name of the currently parsed directory.
    :type dirname: str
    :param names: List of files and directories in the folder.
    :type names: list
    """
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

    :param name: Name of the file.
    :type name: str
    :param dirname: Directory of the file.
    :type dirname: str
    :param options: Program options.
    :type options: object
    :param counts: Suffix statistics.
    :type counts: dict
    :param pattern: Suffix of this file.
    :type pattern: str
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
                make_export(exportfile)

                # Check whether the file was successfully created now.
                if os.path.isfile(exportfile) and _check_time(dirname+"/"+name, exportfile):
                    is_invalid = False


    if is_invalid:
        _mark_invalid(dirname, name, pattern, counts)


def get_makefile_path(result=[]):
    """
    Returns the path to the pattern makefile.

    :param result: Hack for static variable.
    :type result: list
    :return: Path to makefile.
    :rtype: str
    """
    pattern_makefile = "/etc/legacy/patterns.makefile"
    pattern_makefile_user = os.path.expanduser("~/.config/legacy/patterns.makefile")

    if len(result) == 0:
        if os.path.isfile(pattern_makefile_user):
            result.append(pattern_makefile_user)
        elif os.path.isfile(pattern_makefile):
            result.append(pattern_makefile)
        else:
            print("There is no pattern makefile. Please create at either location:")
            print(pattern_makefile)
            print(pattern_makefile_user)
            sys.exit(1)

    return result[0]


def make_export(exportfile):
    """
    Uses a central makefile to create the export file.

    :param exportfile: File to be exported.
    :type exportfile: str
    :return: Whether C{make} returned with success.
    :rtype: bool
    """
    pattern_makefile = get_makefile_path()

    make_command = ["make", "-f", pattern_makefile, "-C", os.path.dirname(exportfile), os.path.basename(exportfile)]

    logging.info(' '.join(make_command))

    try:
        output = subprocess.check_call(make_command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False
    else:
        logging.info(output)
        return True


def _check_time(origfile, exportfile):
    """
    Check whether C{origfile} is older than C{exportfile}.

    :param origfile: Path to first file.
    :type origfile: str
    :param exportfile: Path to second file.
    :type exportfile: str
    :return: Whether first file is older than second.
    :rtype: bool
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

    :param dirname: Directory of the original file.
    :param name: Name of the original file.
    :param exportfile: Expected exportfile.
    :param exportsuffix: Expected suffix of the export file.
    :param options: General program options.
    """
    if not os.path.isfile(exportfile):
        alt_exportfile = dirname+"/"+os.path.splitext(name)[0]+"."+exportsuffix
        if os.path.isfile(alt_exportfile):
            if options.rename:
                os.rename(alt_exportfile, exportfile)
                logging.info("Renaming %s %s", alt_exportfile, exportfile)

            else:
                logging.info("Would rename %s %s", alt_exportfile, exportfile)


def _mark_invalid(dirname, name, pattern, counts):
    """
    Marks a file as having no export.

    :param dirname: Directory of the file.
    :param name: Name of the file.
    :param pattern: Suffix of the original file.
    :param counts: Dict with suffix counts.
    """
    print(os.path.normpath(dirname+"/"+name))

    if not pattern in counts:
        counts[pattern] = 0

    counts[pattern] += 1


def print_summary(counts):
    """
    Prints a statistic.

    :param counts: Dict with C{suffix: counts} pairs.
    """
    if len(counts) == 0:
        return

    print()

    t = prettytable.PrettyTable(["Count", "Suffix", "Name"])
    t.align["Count"] = 'r'
    for row in [[counts[key], key, _patterns[key]["name"]] for key in sorted(counts)]:
        t.add_row(row)
    print(t)


def show_formats():
    """
    Prints a table of all supported formats.
    """
    table = prettytable.PrettyTable(["Suffix", "Name", "Category", "Export Suffixes"])
    table.align = 'l'
    for pattern in sorted(_patterns):
        cur_pattern = _patterns[pattern]
        table_row = []

        table_row.append(pattern)

        if "name" in cur_pattern:
            table_row.append(cur_pattern["name"])
        else:
            table_row.append("")

        if "category" in cur_pattern:
            table_row.append(cur_pattern["category"])
        else:
            table_row.append("")

        if "export_suffixes" in cur_pattern:
            table_row.append(', '.join(sorted(cur_pattern["export_suffixes"])))
        else:
            table_row.append("")

        table.add_row(table_row)

    print(table)
