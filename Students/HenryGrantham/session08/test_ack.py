#!/usr/bin/env python

"""
code that tests ack.py module

can be run with py.test
"""

import pytest  # used for the exception testing

import ack


def test_illegalnumber():
    """An illegal number should return None
    """
    assert ack.ack(-1, 0) is None


def test_stringinsteadofint():
    """A string should raise a TypeError exception.
    """
    with pytest.raises(TypeError):
        assert ack.ack("test", 0)


def test_sequences():
    """Test with first 5 elements of sequences 0 through 4.
    """
    mylist = [[1, 2, 3, 4, 5],
              [2, 3, 4, 5, 6],
              [3, 5, 7, 9, 11],
              [5, 13, 29, 61, 125]]

    for i in range(4):
        for j in range(5):
            assert ack.ack(i, j) == mylist[i][j]
