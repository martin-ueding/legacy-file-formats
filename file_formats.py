#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
This module contains the file type definitions.
"""

__docformat__ = "javadoc en"


import yaml


def get_patterns():
    """
    Get dict with patterns.

    The pattern dict is build up like this
        {suffix: (Long Name, [export suffix, …])}

    @return Pattern dict.
    """

    f = file("default.yaml")
    imported = yaml.load(f)

    patterns = imported["suffixes"]

    return patterns
