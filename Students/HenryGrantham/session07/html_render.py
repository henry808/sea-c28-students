#!/usr/bin/env python

"""
Html package

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """An html element.

    An html element for rendering.
    """
    indent = "    "
    beg_tag = "<>\n"
    end_tag = "</>\n"

    def __init__(self, element=None):
        self.content = []
        if not (element is None):
            self.content.append(element)

    def append(self, element):
        self.content.append(element)

    def render(self, file_out, ind=""):
        file_out.write("{}{}".format(ind, self.beg_tag))
        if type(self) == Element:
            for text in self.content:
                file_out.write("{}{}{}".format(ind, self.indent, text))
                file_out.write("\n")
        elif type(self) == P:
            # this only works for paragraphs with one line.
            file_out.write("{}{}{}".format(ind, self.indent, self.content[0]))
            file_out.write("\n")
        else:
            print self.content
            for content in self.content:
                content.render(file_out, self.indent + ind)
        file_out.write("{}{}".format(ind, self.end_tag))


class Body(Element):
    """A body html element
    """
    beg_tag = "<body>\n"
    end_tag = "</body>\n"


class P(Element):
    """A p html element
    """
    beg_tag = "<p>\n"
    end_tag = "</p>\n"

class Html(Element):
    """A p html element
    """
    beg_tag = "<html>\n"
    end_tag = "</html>\n"
