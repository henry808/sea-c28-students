#!/usr/bin/env python

# lambda_magic.py
#
# Create dictionaries and sets and manipulate them.
from __future__ import print_function


def function_builder(number):
    """Return a list of functions that add 0,1,2,... to a number.


    """
    list_functions = [lambda x, z=i: x+z for i in range(number)]

    # list_functions = []
    # for i in range(number):
    #     list_functions.append(lambda x, z=i: x + z)
    return list_functions

if __name__ == '__main__':

    the_list = function_builder(4)

    print(the_list)

    print(the_list[0](2))
    print("\n")

    print(the_list[1](2))
    print("\n")

    for f in the_list:
        print(f(5))
