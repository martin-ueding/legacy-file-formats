#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
This module contains the file type definitions.
"""

import os
import sys
import yaml

__docformat__ = "restructuredtext en"

def get_patterns():
    """
    Get dict with patterns.

    The pattern dict is build up like this::

        {"suffix":
            {"name": Long Name, "export_suffixes": [export suffix, …]}
            ...
        }

    :return: Pattern dict.
    :rtype: dict
    """
    # TODO Ship some central formats file as a template and fallback.
    filename = "/etc/legacy/formats.yaml"
    filename_user = os.path.expanduser("~/.config/legacy/formats.yaml")
    if not any(map(os.path.isfile, [filename, filename_user])):
        print "Could not find the configuration file."
        print "Please create a YAML file",filename_user
        print "See `man legacy` for more information"
        sys.exit(1)

    

    if os.path.isfile(filename_user):
        f = file(filename_user)
    else:
        f = file(filename)

    imported = yaml.load(f)

    patterns = imported["suffixes"]

    return patterns
