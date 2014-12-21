#!/usr/bin/env python

"""
code that tests ack.py module

can be run with py.test
"""

import pytest  # used for the exception testing

import the_script_comp as scr


def test_inputNone():
    """None should raise a TypeError exception.
    """
    with pytest.raises(TypeError):
        string = None
        assert scr.cleantext(string) is None


def test_inputint():
    """An int should raise a TypeError exception.
    """
    with pytest.raises(TypeError):
        string = 100
        assert scr.cleantext(string) == 100


def test_inputempty():
    """An empty string should return another empty string.
    """
    string = ''
    assert scr.cleantext(string) == ''


def test_inputnoaction():
    """A string with no leading or following spaces should return itself.
    """
    string = 'This is a test of no leading or following spaces.'
    assert scr.cleantext(string) == string


def test_leading():
    """A string with leading spaces should be removed.
    """
    string_beg = '     This is a test of leading spaces.'
    string_end = 'This is a test of leading spaces.'
    assert scr.cleantext(string_beg) == string_end


def test_following():
    """A string with following spaces should be removed.
    """
    string_beg = 'This is a test of following spaces.     '
    string_end = 'This is a test of following spaces.'
    assert scr.cleantext(string_beg) == string_end


def test_leadingandfollowing():
    """A string with leading and following spaces should remove both.
    """
    string_beg = '       This is a test of both.     '
    string_end = 'This is a test of both.'
    assert scr.cleantext(string_beg) == string_end
