#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self):
        self.content = ""
        self.beg_instr = "<>\n"
        self.end_str = "\n</>\n"

    def append(self, text):
        self.content = "{}\n{}".format(self.content, text)

    def render(self, file):
        file.write("{}{}{}".format(self.beg_instr, self.content, self.end_str))
