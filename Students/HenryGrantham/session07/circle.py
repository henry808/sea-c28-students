#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    beg_instr = "<>"
    end_str = "</>"
    string = """<>
    Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
    And here is another piece of text -- you should be able to add any number
</>"""

    def __init__(self):
        pass

    def render(self, text):

        return "".format(beg_instr, text, end_str)