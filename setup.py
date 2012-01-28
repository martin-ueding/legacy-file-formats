#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from distutils.core import setup

setup(
    name = "legacylib",
    author = "Martin Ueding",
    author_email = "dev@martin-ueding.de",
    license = "GPL3",
    version = "1.4",

    packages = ["legacylib"],
    scripts = ["legacy"],
    requires = ["prettytable"],
)
