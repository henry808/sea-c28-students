#!/usr/bin/env python
"""code that tests rot13.py

Can be run with py.test
"""
import math
import pytest  # used for the exception testing

import rot13


def test_empty():

    assert rot13.rot13("") == ""
    # assert rot13(None) == None


def test_numbers():
    """Should not shift and will get the same output as input
    """
    assert rot13.rot13("01234") == "01234"


def test_symbols():
    """Should not shift and will get the same output as input
    """
    assert rot13.rot13("^$&*") == "^$&*"


def test_shifting():
    """Test simple shifting and make sure that case is preserved
    """
    assert rot13.rot13("Hello") == "Uryyb"


def test_mixed():
    """Test simple shifting mixed with numbers.
    """
    assert rot13.rot13("H23ello") == "U23ryyb"


def test_long():
    """Test longer sentence.
    """
    text = "Why did the chicken cross the road?"
    shifted_text = "Jul qvq gur puvpxra pebff gur ebnq?"
    assert rot13.rot13(text) == shifted_text


def test_doubleshift():
    """Test shift dones twice in a row to get back to original text.
    """
    text = "Why did the chicken cross the road?"
    assert rot13.rot13(rot13(text)) == text
