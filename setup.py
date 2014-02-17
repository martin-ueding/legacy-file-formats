#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2014 Martin Ueding <dev@martin-ueding.de>

from setuptools import setup, find_packages

setup(
    author = "Martin Ueding",
    author_email = "dev@martin-ueding.de",
    description = "Finds file formats that might become unreadable.",
    license = "GPL3",
    name = "legacyfileformats",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'legacy-file-formats = legacyfileformats.__init__:main',
        ],
    },
    install_requires=[
        'prettytable',
        'termcolor',
    ],
    url = "https://github.com/martin-ueding/legacy-file-formats",
    version = "1.6.1",
)
