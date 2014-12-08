#!/usr/bin/env python

# safe_input.py
#
# Create dictionaries and sets and manipulate them.


def safe_input(prompt):
    try:
        return raw_input(prompt)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None


if __name__ == '__main__':
    inputs = unicode(safe_input(u"Test prompt: "))
    print inputs