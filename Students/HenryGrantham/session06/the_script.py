#!/usr/bin/env python

# the_script.py
#
# This module contains one function that returns the number of even
# numbers in a list.
import sys
import codecs
import string


def count_evens(nums):
    """Return
    """
    pass


if __name__ == '__main__':
    filename = sys.argv[1]
    f = codecs.open(filename)
    text_data = f.read()
    print(text_data)

    str_list = text_data.split('\n')
    print(str_list)

    end_list = [text.strip() for text in str_list]

    print(end_list)

    text_data = '\n'.join(end_list)

    print(text_data)

    while True:
        promptstr = u"Your file has been cleaned of leading"
                    u"and trailing spaces\n"
                    u"Would you like to\n"
                    u"1 Save over the same file\n"
                    u"2 Write to a new file\n"
                    u"(list for list; q for menu)?"
        donor = unicode(raw_input(promptstr))

    f.close()
    print("Closed file.")
