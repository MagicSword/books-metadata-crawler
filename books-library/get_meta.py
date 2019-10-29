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

    def  refineData(self):
        pass

"""
def cli():
    "Command-line interface (looks at sys.argv to decide what to do)."
    import getopt
    class BadUsage: pass

    # Scripts don't get the current directory in their path by default
    # unless they are run with the '-m' switch
    if '' not in sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, '.')

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'gk:p:w')
        writing = 0

        for opt, val in opts:
            if opt == '-g':
                gui()
                return
            if opt == '-k':
                apropos(val)
                return
            if opt == '-p':
                try:
                    port = int(val)
                except ValueError:
                    raise BadUsage
                def ready(server):
                    print 'pydoc server ready at %s' % server.url
                def stopped():
                    print 'pydoc server stopped'
                serve(port, ready, stopped)
                return
            if opt == '-w':
                writing = 1

        if not args: raise BadUsage
        for arg in args:
            if ispath(arg) and not os.path.exists(arg):
                print 'file %r does not exist' % arg
                break
            try:
                if ispath(arg) and os.path.isfile(arg):
                    arg = importfile(arg)
                if writing:
                    if ispath(arg) and os.path.isdir(arg):
                        writedocs(arg)
                    else:
                        writedoc(arg)
                else:
                    help.help(arg)
            except ErrorDuringImport, value:
                print value

    except (getopt.error, BadUsage):
        cmd = os.path.basename(sys.argv[0])
        print "pydoc - the Python documentation tool
%s <name> ...
    Show text documentation on something.  <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package.  If <name> contains a '%s', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.
%s -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.
%s -p <port>
    Start an HTTP server on the given port on the local machine.  Port
    number 0 can be used to get an arbitrary unused port.
%s -g
    Pop up a graphical interface for finding and serving documentation.
%s -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '%s', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.
" % (cmd, os.sep, cmd, cmd, cmd, cmd, os.sep)
"""


if __name__ == '__main__':
    bo = NewBook('0010836923')
    print("![" + bo.title + "](" + bo.imageurl + ' =50%x50%)')
    print("* [圖書資料](" + bo.url + ")")
    print(bo.description)

