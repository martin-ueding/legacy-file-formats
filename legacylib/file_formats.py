#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
This module contains the file type definitions.
"""

import os
import sys
import yaml

def get_patterns():
    """
    Get dict with patterns.

    The pattern dict is build up like this::

        {"suffix":
            {"name": Long Name, "export_suffixes": [export suffix, …]}
            ...
        }

    @return: Pattern dict.
    @rtype: dict
    """
    filename = os.path.expanduser("~/.config/legacy/formats.yaml")
    if not os.path.isfile(filename):
        print "Could not find the configuration file."
        print "Please create a YAML file",filename
        print "See `man legacy` for more information"
        sys.exit(1)

    f = file(filename)
    imported = yaml.load(f)

    patterns = imported["suffixes"]

    return patterns
