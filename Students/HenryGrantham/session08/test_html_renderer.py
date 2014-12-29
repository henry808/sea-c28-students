#!/usr/bin/env python

"""
code that tests html_renderer.py module

can be run with py.test
"""

import cStringIO

import pytest  # used for the exception testing

import html_render as hr


def test_Element():
    """Test Element
    """
    page = hr.Element()

    page.append(u"Here is a paragraph of text")

    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u"<>",
             u"    Here is a paragraph of text",
             u"    And here is another piece of text",
             u"</>",
             u""]

    compare = "\n".join(lines)

    # use this code to see what happens in the renderer.
    # print('rendered_string:')
    # print(rendered_string)
    # print('compared string:')
    # print(compare)

    assert isinstance(page, hr.Element)
    assert rendered_string == compare


def test_ElementAttributes():
    """Test Element Class with attributes

    This tests attributes
    """
    page = hr.Element(u"This is a test.",
                      style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")
    page.append(u"And here is a second piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'< style="text-align: center; font-style: oblique;">',
             u"    This is a test.",
             u"    And here is another piece of text",
             u"    And here is a second piece of text",
             u"</>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.Element)
    assert rendered_string == compare


def test_Body():
    """Test Body Class with attributes

    This tests Body Class and attributes
    """
    page = hr.Body(u"This is a test.",
                   style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<body style="text-align: center; font-style: oblique;">',
             u"    This is a test.",
             u"    And here is another piece of text",
             u"</body>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.Body)
    assert rendered_string == compare


def test_P():
    """Test P Class with attributes

    This tests P Class and attributes
    """
    page = hr.P(u"Here is a paragraph of text",
                style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<p style="text-align: center; font-style: oblique;">',
             u"    Here is a paragraph of text",
             u"    And here is another piece of text",
             u"</p>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.P)
    assert rendered_string == compare


def test_Head():
    """Test Head Class with attributes

    This tests Head Class and attributes
    """
    page = hr.Head(u"This is a test.",
                   style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<head style="text-align: center; font-style: oblique;">',
             u"    This is a test.",
             u"    And here is another piece of text",
             u"</head>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.Head)
    assert rendered_string == compare


def test_Ul():
    """Test Ul Class with attributes

    This tests Ul Class and attributes
    """
    page = hr.Ul(u"This is a test.",
                 style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<ul style="text-align: center; font-style: oblique;">',
             u"    This is a test.",
             u"    And here is another piece of text",
             u"</ul>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.Ul)
    assert rendered_string == compare


def test_Li():
    """Test Li Class with attributes

    This tests Li Class and attributes
    """
    page = hr.Li(u"This is a test.",
                 style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<li style="text-align: center; font-style: oblique;">',
             u"    This is a test.",
             u"    And here is another piece of text",
             u"</li>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.Li)
    assert rendered_string == compare


def test_Html():
    """Test Html Class with attributes

    This tests Html Class and attributes
    """
    page = hr.Html(u"This is a test.",
                   style=u"text-align: center; font-style: oblique;")
    page.append(u"And here is another piece of text")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u"<!DOCTYPE html>",
             u'<html style="text-align: center; font-style: oblique;">',
             u"    This is a test.",
             u"    And here is another piece of text",
             u"</html>",
             u""]

    compare = "\n".join(lines)

    assert isinstance(page, hr.Html)
    assert rendered_string == compare


def test_OneLineTag():
    """Test OneLineTag Class with attributes

    This tests OneLineTag Class and attributes
    """
    page = hr.OneLineTag(u"This is a one line test.",
                         style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<OneLineTag style="text-align: center; font-style: oblique;">',
             u"This is a one line test.",
             u"</OneLineTag>"]

    compare = "{}\n".format("".join(lines))

    assert isinstance(page, hr.OneLineTag)
    assert rendered_string == compare


def test_Title():
    """Test Title Class with attributes

    This tests Title Class and attributes
    """
    page = hr.Title(u"This is a one line test.",
                    style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<title style="text-align: center; font-style: oblique;">',
             u"This is a one line test.",
             u"</title>"]

    compare = "{}\n".format("".join(lines))

    assert isinstance(page, hr.Title)
    assert rendered_string == compare


def test_H():
    """Test Header Class with attributes

    This tests Header Class and attributes
    """
    page = hr.H(4, u"This is a one line test.",
                style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<h4 style="text-align: center; font-style: oblique;">',
             u"This is a one line test.",
             u"</h4>"]

    compare = "{}\n".format("".join(lines))

    assert isinstance(page, hr.H)
    assert rendered_string == compare


def test_SelfClosingTag():
    """Test SelfClosingTag Class with attributes

    This tests SelfClosingTag Class and attributes
    """
    page = hr.SelfClosingTag(style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<SelfClosingTag style="text-align: center; font-style: oblique;"',
             u" />\n"]

    compare = "{}".format("".join(lines))

    assert isinstance(page, hr.SelfClosingTag)
    assert rendered_string == compare


def test_Hr():
    """Test Hr Class with attributes

    This tests Hr Class and attributes
    """
    page = hr.Hr(style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<hr style="text-align: center; font-style: oblique;"',
             u" />\n"]

    compare = "{}".format("".join(lines))

    assert isinstance(page, hr.Hr)
    assert rendered_string == compare


def test_Br():
    """Test Br Class with attributes

    This tests Br Class and attributes
    """
    page = hr.Br(style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<br style="text-align: center; font-style: oblique;"',
             u" />\n"]

    compare = "{}".format("".join(lines))

    assert isinstance(page, hr.Br)
    assert rendered_string == compare


def test_Meta():
    """Test Meta Class with attributes

    This tests Meta Class and attributes
    """
    page = hr.Meta(style=u"text-align: center; font-style: oblique;")

    f = cStringIO.StringIO()
    page.render(f)
    rendered_string = f.getvalue()

    lines = [u'<meta style="text-align: center; font-style: oblique;"',
             u" />\n"]

    compare = "{}".format("".join(lines))

    assert isinstance(page, hr.Meta)
    assert rendered_string == compare


# Use this when implementing OneLineTag that works correctly.
# I am going to fix this on another git branch (session07) where
# the real html_renderer.py lives.
#
# def test_OneLineTag_Multiple_Elements():
#     """Test OneLineTag Class with multiple elements and attributes

#     This tests OneLineTag Class and attributes
#     """
#     page = hr.OneLineTag(u"This is a one line test.",
#                          style=u"text-align: center; font-style: oblique;")
#     # page.append(u"And here is another piece of text")

#     f = cStringIO.StringIO()
#     page.render(f)
#     rendered_string = f.getvalue()

#     lines = [u'<OneLineTag style="text-align: center; font-style: oblique;">',
#              u"This is a one line test.",
#     #         u"    And here is another piece of text",
#              u"</OneLineTag>"]

#     compare = "{}\n".format("".join(lines))

#     print('rendered_string:')
#     print(rendered_string)
#     print('compared string:')
#     print(compare)

#     assert rendered_string == compare
    # <a href="someplace.html">There is a <span class="funny">styled sub-element</span>

