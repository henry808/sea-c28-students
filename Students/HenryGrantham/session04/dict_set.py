#!/usr/bin/env python

# dict_set.py
#
# Create dictionaries and sets and manipulate them.


if __name__ == '__main__':
    d = {'name': 'Chris',
         'city': 'Seattle',
         'cake': 'Chocolate'}
    # print dictionary
    for k, v in d.items():
        print(k)
        print(v)
    print("\n")

    # delete entry
    d.pop('cake')

    # print dictionary
    for k, v in d.items():
        print(k)
        print(v)
    print("\n")

    # add entry
    d['fruit'] = 'Mango'

    # print dictionary
    for k, v in d.items():
        print(k)
        print(v)
    print("\n")

    # print keys and values
    print(d.keys())
    print(d.values())
    print("\n")

    # print whether or not cake is a key in the dictionary.
    print 'cake' in d.keys()
    # print whether or not Mango is a value in the dictionary.
    print 'Mango' in d.values()

    # Make a dictionary with 0..15 as keys and hex equivelant as values
    intlist = range(16)
    hexlist = range(16)

    for i in hexlist:
        hexlist[i] = hex(i)

    inthexdict = dict(zip(intlist, hexlist))

    print(inthexdict.items())

    # Using same dictionary, change values to key # of a's
    for k in inthexdict.keys():
        inthexdict[k] = 'a' * k

    print(inthexdict.items())

    # Sets s2, s3 and s4 contain #'s from
    #     0 through 20, divisible 2, 3 and 4.
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(21):
        if i / 2 == float(i) / 2:
            s2.add(i)
        if i / 3 == float(i) / 3:
            s3.add(i)
        if i / 4 == float(i) / 4:
            s4.add(i)
    # Display sets
    print(s2)
    print(s3)
    print(s4)

    # Display if s3 is a subset of s2
    print s3.issubset(s2)
    # Display if s4 is a subset of s2
    print s4.issubset(s2)

    # Create a set of letters of Python
    setofstrings = set("Python")
    setofstrings.add('i')
    print(setofstrings)

    # Create a frozenset of letters in 'marathon'
    fsetofstrings = set('marathon')
    print(fsetofstrings)
    print setofstrings.union(fsetofstrings)
    print setofstrings.intersection(fsetofstrings)
