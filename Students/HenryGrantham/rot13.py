#!/usr/bin/env python

# ROT13 ENCRYPTION MODULE
#
# This module.


def rot_letter(text):
    """Given a letter, return a letter 13 letters after it.

    text is the letter to rotate.
    if text is not a letter or has nothing in it, then return None.
    if the sting is longer than 1 character than only use the first
        character.
    if text is a space, then return a space.
    if text is a capital letter than returns a capital letter
        13 letters after it, wrapping around after z.
    if text is a small case letter than  returns a small case letter
        13 letters after it, wrapping around after z.
    """
    if text is None:
        print(u"The string is None.")
        return None
    if text == "":
        print(u"The string has nothing in it.")
        return None
    text = text[0]
    if text.isspace():
        return text
    elif text.isalpha():
        print text
        return text
    else:
        print(u"The string does not contain a letter.")
        return None


def rot13(text):
    """Given a string, return a ROT13 encoded string.

    text is the string to encode.
    if text does not concatain all letters then return None.
    """
    if text.isalpha():
        pass
    else:
        print(u"The string does not contain all letters.")
        return None

if __name__ == '__main__':
    # Testing rot13_letter
    # check for case where string is empty or contains a number
    #   or symbol or space or is None

    assert rot_letter(None) is None
    assert rot_letter("") is None
    assert rot_letter("0") is None
    assert rot_letter("^") is None
    assert rot_letter("i") == "i"

    print(rot_letter("i"))

