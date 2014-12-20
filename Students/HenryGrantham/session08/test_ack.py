#!/usr/bin/env python

"""
code that tests ack.py module

can be run with py.test
"""

import pytest  # used for the exception testing

import ack


def test_illegal():
    """An illegal number should return None
    """
    assert ack.ack(-1, 0) is None


def test_inputstr():
    """A string should raise a TypeError exception.
    """
    with pytest.raises(TypeError):
        assert ack.ack("test", 0)


def test_inputstr0i():
    """Test with 0 and i where i is 0 to 4
    """
    mylist = [1, 2, 3, 4, 5]
    for i in range(4):
        assert ack.ack(0, i) == mylist[i]


def test_inputstr1i():
    """Test with 1 and i where i is 0 to 4
    """
    mylist = [2, 3, 4, 5, 6]
    for i in range(4):
        assert ack.ack(1, i) == mylist[i]


def test_inputstr2i():
    """Test with 2 and i where i is 0 to 4
    """
    mylist = [3, 5, 7, 9, 11]
    for i in range(4):
        assert ack.ack(2, i) == mylist[i]


def test_inputstr3i():
    """Test with 3 and i where i is 0 to 4
    """
    mylist = [5, 13, 29, 61, 125]
    for i in range(4):
        assert ack.ack(3, i) == mylist[i]
