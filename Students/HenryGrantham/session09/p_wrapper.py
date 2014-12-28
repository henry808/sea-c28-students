#!/usr/bin/env python
# -*- coding: utf-8 -*-


def p_wrapper(func):
    """Wraps original output in an HTML 'p' tag
    """
    def wrapped(text):
        return u"<p> {} </p>".format(func(text))
    return wrapped


@p_wrapper
def return_a_string(string):
    """Returns a string
    """
    return string

if __name__ == '__main__':
    pass
    # string = "Test."
    # print(return_a_string(string))
