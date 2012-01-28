#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from distutils.core import setup

setup(
    author = "Martin Ueding",
    author_email = "dev@martin-ueding.de",
    license = "GPL3",
    name = "legacylib",
    packages = ["legacylib"],
    requires = ["prettytable"],
    scripts = ["legacy"],
    version = "1.4",
)
