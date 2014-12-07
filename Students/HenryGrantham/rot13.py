#!/usr/bin/env python

# ROT13 ENCRYPTION MODULE
#
# This module.


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

    table = None
    return text.translate(table)


if __name__ == '__main__':
    # Testing ROT13
    # check for case where string is empty or contains a number
    #   or symbol or space or is None

    assert rot13(None) is None
    assert rot13("") == ""
    assert rot13("01234") == "01234"
    assert rot13("^$&*") == "^$&*"
    assert rot13("This is a test") == "This is a test"

    print(rot13("This is a test"))

