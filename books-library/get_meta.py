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
# TODO: add  cli()
#

from BaseClass import Book
import requests
from bs4 import BeautifulSoup
import re
import click

# --------------------------------------------------------- common routines
# https://www.books.com.tw/products/0010836923

"""
url = 'https://www.books.com.tw/products/0010836923'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find("meta",  property="og:title")
url = soup.find("meta",  property="og:url")
description = soup.find("meta",  property="og:description")
image = soup.find("meta",  property="og:image")

pattern= "(https:\/\/www).*.*(jpg)"



print(title["content"] if title else "No meta title given")
print(url["content"] if url else "No meta url given")
print(image["content"] if image else "No meta url given")
print(description["content"] if description else "No meta url given")
"""

class NewBook(Book):
    def __init__(self,id):
        self.id = id
        self.title = ''
        self.description = ''
        self.imageurl = ''
        self.getData()

    def getData(self):
        url = 'https://www.books.com.tw/products/' + self.id
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.title = soup.find("meta", property="og:title")["content"]
        self.url = soup.find("meta", property="og:url")["content"]
        image = soup.find("meta", property="og:image")["content"]
        self.imageurl = re.search(r'(https:\/\/www).*.*(jpg)', image).group(0)
        desc = soup.find("meta", property="og:description")["content"]
        description = ''
        for li in desc.split('，'):
            new_li = ''.join(('* ', li, '\n'))
            description = description + new_li
        self.description = description



@click.command()
@click.option('-b', '--bookid', help='Books book id', default='0010804030')
def publishMD(bookid):
    "Output book data as Markdown format"
    bo = NewBook(bookid)
    print("![" + bo.title + "](" + bo.imageurl + ' =50%x50%)')
    print("* [圖書資料](" + bo.url + ")")
    print(bo.description)



if __name__ == '__main__':
    publishMD()

