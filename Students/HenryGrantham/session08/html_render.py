#!/usr/bin/env python

"""
Html package

This is a package with classes that represent html elements and
An html page can be generated from them.

"""


class Element(object):
    """An html element.

    An html element for rendering.
    """
    indent = "    "
    tag = ""

    def __init__(self, element=None, **kwargs):
        self.content = []
        if element:
            self.content.append(unicode(element))
        self.attributes = kwargs
        super(Element, self).__init__()

    def getattributes(self):
        """Returns a string of attributes given an element
        """
        if self.attributes:
            att_list = [' {}="{}"'.format(k, self.attributes[k])
                        for k in self.attributes]
            return "; ".join(att_list)
        else:
            return ''

    def append(self, element):
        """Add an element to this list's element
        """
        self.content.append(element)

    def render(self, file_out, ind=""):
        """Render into an IO stream the html element.

        This is a recursive method that builds the html web page.
        """
        att_string = self.getattributes()
        file_out.write("{}<{}{}>\n".format(ind, self.tag, att_string))
        for content in self.content:
            if isinstance(content, unicode):
                file_out.write("{}{}{}\n".format(ind, self.indent, content))
            else:
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

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>\n")
        super(Html, self).render(file_out, ind)


class Head(Element):
    """A Head html element
    """
    tag = "head"


class OneLineTag(Element):
    """A OneLineTag html element
    """
    tag = "OneLineTag"

    def render(self, file_out, ind=""):
        att_string = self.getattributes()
        file_out.write("{}<{}{}>{}</{}>\n".format(ind,
                                                  self.tag,
                                                  att_string,
                                                  self.content[0],
                                                  self.tag))


class Title(OneLineTag):
    """A OneLineTag html element
    """
    tag = "title"


class SelfClosingTag(Element):
    """A SelfClosingTag html element
    """
    tag = "SelfClosingTag"

    def render(self, file_out, ind=""):
        att_string = self.getattributes()
        file_out.write("{}<{}{} />\n".format(ind, self.tag, att_string))


class Hr(SelfClosingTag):
    """A Hr element (horizontal rule)
    """
    tag = "hr"


class Br(SelfClosingTag):
    """A Br element ( linebreak)
    """
    tag = "br"


class A(OneLineTag):
    """A link element
    """
    tag = "a"

    def __init__(self, link, content):
        super(A, self).__init__(unicode(content), href=link)


class H(OneLineTag):
    """A header element
    """
    tag = "h"

    def __init__(self, integer, element=None, **kwargs):
        self.tag = "{}{}".format(self.tag, integer)
        super(H, self).__init__(element, **kwargs)


class Ul(Element):
    """An unordered element
    """
    tag = "ul"


class Li(Element):
    """A list element
    """
    tag = "li"


class Meta(SelfClosingTag):
    """A meta element
    """
    tag = "meta"
