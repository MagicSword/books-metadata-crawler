#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Name of this command

DESCRIPTION here

"""
__all__ = ['help']
__author__ = "Nero <magicsword@gmail.com>"
__date__ = "26 February 2001"
__copyright__ = "Copyright 2017, The Nostalgic project"
__license__ = "MPL 2.0"
__version__ = "0.1.0"
__maintainer__ = "Nero"
__status__ = "Dev"
__credits__ = """Bleo, bleo bleo blue.
Bleo, bleo bleo blue.
"""

# Known bugs that can't be fixed here:
#   - synopsis() cannot be prevented from clobbering existing
#     loaded modules.
#   - If the __file__ attribute on a module is a relative path and
#     the current directory is changed with os.chdir(), an incorrect
#     path will be displayed.

import abc


# --------------------------------------------------------- common routines


# ---------------------------------------------------- formatter base class

class Media(abc.ABC):
    """Base class of medias"""
    pass


class Video(Media):
    """class for Videos discs"""
    pass

class Book(Media):
    """Book class"""
    def __init__(self,id):
        self.id = id
        self.isbn = ''
        self.title = ''
        self.subtitle = ''
        self.name_ori = ''
        self.author = ''
        self.author_other = ''
        self.publication_date = ''
        self.publisher = ''
        self.price = ''
        self.price_current = ''
        self.format = '' #paperback/softcover/hardcover
        self.pages = ''
        self.language = ''
        self.category = ''
        self.dimensions = ''  # 大小
        self.distribution_Area = ''
        self.summary = ''
        self.author_about = ''
        self.toc = ''
    def __str__(self):
        return self.title
    def __repr__(self):
        #return self.title + ' ' + self.subtitle
        return self.title
    def __len__(self):
        #return self.pages
        pass
    def __eq__(self, other):
        #return self.title == other.title and self.author == other.author and self.id == other.id
        pass

