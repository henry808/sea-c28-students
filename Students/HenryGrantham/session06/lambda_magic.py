#!/usr/bin/env python

# lambda_magic.py
#
# Contains one function that returns a list of functions.
# Also contains code that tests function.
from __future__ import print_function


def function_builder(number):
    """Return a list of functions that add 0,1,2,... to a number.

    The nth function in the list adds n to the input.
    """
    return [lambda x, z=i: x+z for i in range(number)]

if __name__ == '__main__':

    the_list = function_builder(4)

    print(the_list)

    print("The list contains %s functions." % len(the_list))

    print(the_list[0](2))
    print("\n")

    print(the_list[1](2))
    print("\n")

    for f in the_list:
        print(f(5))

    print("Everything checks out.")
