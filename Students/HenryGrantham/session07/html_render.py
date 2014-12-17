#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """An html element.

    An html element for rendering.
    """
    indent = "   "

    def __init__(self):
        self.content = ""
        self.beg_tag = "<>\n"
        self.end_tag = "</>\n"

    def append(self, text):
        self.content = "{}\n{}".format(self.content, text)

    def render(self, file_out, ind="    "):
        self.content = self.content.replace("\n", "\n" + self.indent + ind)
        file_out.write("{id}{}{}\n{id}{}".format(self.beg_tag,
                                                 self.content,
                                                 self.end_tag,
                                                 id=ind))
