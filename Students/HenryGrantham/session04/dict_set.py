#!/usr/bin/env python

# dict_set.py
#
# Create a dictionary and manipulate it.


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

    # Make a dictionary with 0..15 as keys and # of a's as values
    for i in range(len(hexlist)):
        hexlist[i] = 'a' * i

    inthexdict = dict(zip(intlist, hexlist))

    print(inthexdict.items())


