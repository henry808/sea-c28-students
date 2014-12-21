#!/usr/bin/env python

"""
code that tests html_renderer.py module

can be run with py.test
"""
import codecs
import cStringIO

import pytest  # used for the exception testing

import html_render as hr

# writing the file out:
def render(page, filename):
   """
   render the tree of elements

   This uses cSstringIO to renderto memory, then dump to console and
   write to file -- very handy!
   """

   f = cStringIO.StringIO()
   page.render(f)

   f.reset()

   print f.read()

   f.reset()
   codecs.open(filename, 'w', encoding="utf-8").write( f.read() )

# test step1
def test_renderstep1():
    """
    render the tree of elements

    This uses cSstringIO to renderto memory, then dump to console and
    write to file -- very handy!
    """
    page = hr.Element()

    page.append(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")

    page.append(u"And here is another piece of text -- you should be able to add any number")

    render(page, u"test_html_output1.html")

    print(page)

    assert True


# test step2
def test_renderstep2():
    page = hr.Html()

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

    body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))

    page.append(body)

    render(page, u"test_html_output2.html")

    assert True


# test step3
def test_renderstep3():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
    body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))

    page.append(body)

    render(page, u"test_html_output3.html")

    assert True


# test step4
def test_renderstep4():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style=u"text-align: center; font-style: oblique;"))

    page.append(body)

    render(page, u"test_html_output4.html")

    assert True


# test step5
def test_renderstep5():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    page.append(body)

    render(page, u"test_html_output5.html")
    assert True


# test step6
def test_renderstep6():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                 style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    body.append(u"And this is a ")
    body.append(hr.A(u"http://google.com", "link") )
    body.append(u"to google")

    page.append(body)

    render(page, u"test_html_output6.html")
    assert True


# test step7
def test_renderstep7():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.H(2, u"PythonClass - Class 6 example"))

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                 style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    list = hr.Ul(id=u"TheList", style=u"line-height:200%")

    list.append(hr.Li(u"The first item in a list"))
    list.append(hr.Li(u"This is the second item", style="color: red"))

    item = hr.Li()
    item.append(u"And this is a ")
    item.append(hr.A(u"http://google.com", u"link"))
    item.append(u"to google")

    list.append(item)

    body.append(list)

    page.append(body)

    render(page, u"test_html_output7.html")
    assert True


# test step8
def test_renderstep8():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Meta(charset=u"UTF-8"))
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.H(2, u"PythonClass - Class 6 example"))

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                 style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    list = hr.Ul(id=u"TheList", style=u"line-height:200%")

    list.append(hr.Li(u"The first item in a list"))
    list.append(hr.Li(u"This is the second item", style="color: red"))

    item = hr.Li()
    item.append(u"And this is a ")
    item.append(hr.A(u"http://google.com", "link"))
    item.append(u"to google")

    list.append(item)

    body.append(list)

    page.append(body)

    render(page, u"test_html_output8.html")
    assert True
