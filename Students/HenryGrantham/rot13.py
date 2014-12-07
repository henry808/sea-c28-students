#!/usr/bin/env python

# ROT13 ENCRYPTION MODULE
#
# This module performs ROT13 to a string. It will replace every letter
# in the string to 13th letter after in in the alphabet and wraps around at z.

from string import maketrans


def rot13(text):
    """Given a string, return a ROT13 encoded string.

    text is the string to encode.

    if text is None return None
    if string is empty, return an empty string.

    Everything that is not a letter in text will not be changed.
    All letters in this string will be shifted 13 letters forward,
        wrapping around after z with capital vs. small cased letters
        preserved.
    """
    if text is None:
        return None

    table = maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                      "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    return text.translate(table)


if __name__ == '__main__':
    # Testing ROT13
    # check for case where string is empty or contains a number
    #   or symbol or space or is None

    assert rot13(None) is None
    assert rot13("") == ""
    assert rot13("01234") == "01234"
    assert rot13("^$&*") == "^$&*"

    # Testing ROT13
    # check to see if shift works and make sure that all nonstring
    # characters are preserved.
    assert rot13("Hello") == "Uryyb"
    assert rot13(rot13("Hello")) == "Hello"
    assert rot13("Why did the chicken cross the road?") == "Jul qvq gur " \
        "puvpxra pebff gur ebnq?"

    assert rot13(rot13("Why did the chicken cross the road?")) == "Why " \
        "did the chicken cross the road?"
