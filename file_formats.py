#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
This module contains the file type definitions.
"""

__docformat__ = "javadoc en"


import os
import sys
import yaml


def get_patterns():
    """
    Get dict with patterns.

    The pattern dict is build up like this
        {suffix: (Long Name, [export suffix, …])}

    @return Pattern dict.
    """
    filename = os.path.expanduser("~/.legacy.yaml")
    if not os.path.isfile(filename):
        print "Could not find the configuration file."
        print "Please create a YAML file",filename
        print "See `man legacy` for more information"
        sys.exit(1)

    f = file(filename)
    imported = yaml.load(f)

    patterns = imported["suffixes"]

    return patterns
