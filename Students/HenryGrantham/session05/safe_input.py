#!/usr/bin/env python

# safe_input.py
#
# Prompt wrapper function that blocks the use of ^C and ^D (^Z on Windows).


def safe_input(prompt):
    """Prompt that blocks the use of ^C and ^D.

    ^C normally causes a KeyboardInterrupt Error and ^D (^Z on Windows)
    usually causes an End Of File Error, but this wrapper file blocks
    those errors from ending the program.

    """
    try:
        return raw_input(prompt)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None


if __name__ == '__main__':
    inputs = unicode(safe_input(u"Test prompt: "))
    print inputs
