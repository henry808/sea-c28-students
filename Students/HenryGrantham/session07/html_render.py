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
    tag = ""

    def __init__(self, element=None, **kwargs):
        self.content = []
        if not (element is None):
            self.content.append(element)
        self.attributes = kwargs

    def append(self, element):
        self.content.append(element)

    def render(self, file_out, ind=""):
        if not(len(self.attributes) == 0):
            att_list = ["{}={}".format(k, self.attributes[k]) for k in self.attributes]
            att_string = "; ".join(att_list)
        else:
            att_string = ''
        file_out.write("{}<{}{}>\n".format(ind, self.tag, att_string))
        if type(self) == Element:
            for text in self.content:
                file_out.write("{}{}{}".format(ind, self.indent, text))
                file_out.write("\n")
        elif type(self) == P:
            # this only works for paragraphs with one line.
            file_out.write("{}{}{}".format(ind, self.indent, self.content[0]))
            file_out.write("\n")
        else:
            for content in self.content:
                content.render(file_out, self.indent + ind)
        file_out.write("{}</{}>\n".format(ind, self.tag))


class Body(Element):
    """A body html element
    """
    tag = "body"


class P(Element):
    """A P html element
    """
    tag = "p"


class Html(Element):
    """A Html element
    """
    tag = "html"


class Head(Element):
    """A Head html element
    """
    tag = "head"


class OneLineTag(Element):
    """A OneLineTag html element
    """
    tag = "OneLineTag"


class Title(Element):
    """A OneLineTag html element
    """
    tag = "title"

    def render(self, file_out, ind=""):
        file_out.write("{}<{}>".format(ind, self.tag))
        file_out.write("{}".format(self.content[0]))
        file_out.write("</{}>\n".format(self.tag))

