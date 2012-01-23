#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
This module contains the file type definitions.
"""

__docformat__ = "javadoc en"

def get_patterns():
    """
    Get dict with patterns.

    The pattern dict is build up like this
        {suffix: (Long Name, [export suffix, …])}

    @return Pattern dict.
    """

    # Export format groups for various file types.
    type_audio = ["mp3", "ogg", "flac"]
    type_disk_image = ["iso", "zip"]
    type_drawing = ["pdf", "svg", "eps", "ps"]
    type_picture = ["png", "tiff", "tif", "bmp"]
    type_presentation = ["pdf"]
    type_tabular = ["pdf", "csv"]
    type_text = ["pdf", "txt", "rtf", "markdown", "tex", "md"]
    type_video = ["ogv", "avi", "mpg", "mp4"]

    # Dict of file extensions that should be checked. The full name is for the
    # stats output. The second element in the details tuple is a list of
    # alternative file formats that satisfy the export as well.
    patterns = {
        "cdr": ("Corel Draw", type_drawing),
        "dmg": ("Apple Disk Image", type_disk_image),
        "doc": ("Microsoft Word", type_text),
        "docx": ("Microsoft Word", type_text),
        "flv": ("Flash Video", type_video),
        "indd": ("Adobe InDesign", type_drawing),
        "key": ("Apple Keynote", type_presentation),
        "mindnode": ("Mindnode Mindmap", ["pdf"]),
        "mw": ("Maple Worksheet", ["pdf"]),
        "nb": ("Mathematica Notebook", ["pdf"]),
        "numbers": ("Apple Numbers", type_tabular),
        "odg": ("OpenOffice Draw", type_drawing),
        "odp": ("OpenOffice Impress", type_presentation),
        "ods": ("OpenOffice Calc", type_tabular),
        "odt": ("OpenOffice Writer", type_text),
        "pages": ("Apple Pages", type_text),
        "ppsx": ("Microsoft PowerPoint", type_presentation),
        "ppt": ("Microsoft PowerPoint", type_presentation),
        "ppts": ("Microsoft PowerPoint", type_presentation),
        "pptx": ("Microsoft PowerPoint", type_presentation),
        "psd": ("Adobe Photoshop", type_picture),
        "rtfd": ("Rich Text Format Directory", type_text),
        "webarchive": ("Safari Web Archive", ["pdf", "html"]),
        "wma": ("Windows Media Audio", type_audio),
        "wmv": ("Windows Media Video", type_video),
        "xcf": ("GIMP Picture", type_picture),
        "xls": ("Microsoft Excel", type_tabular),
        "xlsx": ("Microsoft Excel", type_tabular),
        "xoj": ("Xournal", type_drawing),
    }

    return patterns
