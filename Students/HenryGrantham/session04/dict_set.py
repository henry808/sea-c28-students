#!/usr/bin/env python

# dict_set.py
#
# Create dictionaries and sets and manipulate them.
from __future__ import print_function

if __name__ == '__main__':
    d = {'name': 'Chris',
         'city': 'Seattle',
         'cake': 'Chocolate'}
    # print dictionary
    print(d)

    # delete entry
    d.pop('cake')

    # print dictionary
    print(d)

    # add entry
    d['fruit'] = 'Mango'

    # print dictionary
    print(d)

    # print keys and values
    print(d.keys())
    print(d.values())
    print("\n")

    # print whether or not cake is a key in the dictionary.
    print ('cake' in d)
    # print whether or not Mango is a value in the dictionary.
    print ('Mango' in d.values())

    # Make a dictionary with 0..15 as keys and hex equivelant as values
    intlist = range(16)
    hexlist = range(16)

    for i in hexlist:
        hexlist[i] = hex(i)

    inthexdict = dict(zip(intlist, hexlist))

    print(inthexdict.items())

    # Using part 1 dictionary, count # of a's in the values and set
    #   to the new value.
    for k in d:
        d[k] = d[k].count('a')
    print(d)

    # Sets s2, s3 and s4 contain #'s from
    #     0 through 20, divisible 2, 3 and 4.
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(21):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i)
        if i % 4 == 0:
            s4.add(i)
    # Display sets
    print(s2)
    print(s3)
    print(s4)

    # Display if s3 is a subset of s2
    print(s3.issubset(s2))
    # Display if s4 is a subset of s2
    print(s4.issubset(s2))

    # Create a set of letters of Python
    setofstrings = set("Python")
    setofstrings.add('i')
    print(setofstrings)

    # Create a frozenset of letters in 'marathon'
    fsetofstrings = set('marathon')
    print(fsetofstrings)
    print(setofstrings.union(fsetofstrings))
    print(setofstrings.intersection(fsetofstrings))
