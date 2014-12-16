#!/usr/bin/env python

# dict_set.py
#
# Create dictionaries and sets and manipulate them.
from __future__ import print_function


# print dictionary
def print_dict(food_prefs):
    """Print the dictionary
    """
    text = "{} is from {}, and he likes ".format(food_prefs['name'],
                                                 food_prefs['city'])
    text += "{} cake, {} fruit, {} salad, and {} pasta." \
        .format(food_prefs['cake'],
                food_prefs['fruit'],
                food_prefs['salad'],
                food_prefs['pasta'])
    print(text)


if __name__ == '__main__':
    food_prefs = {u"name": u"Cris",
                  u"city": u"Seattle",
                  u"cake": u"lemon",
                  u"fruit": u"pomegranate",
                  u"salad": u"chop",
                  u"pasta": u"lasagna"}

    # print dictionary
    print_dict(food_prefs)

    # Make a dictionary with 0..15 as keys and hex equivelant as values
    # using list comprehensions
    intlist = [x for x in range(16)]
    hexlist = [hex(x) for x in range(16)]
    inthexdict = dict(zip(intlist, hexlist))

    print(inthexdict)

    # Make a dictionary with 0..15 as keys and hex equivelant as values
    # using dict comprehensions
    inthexdict = {i: hex(i) for i in range(16)}

    print(inthexdict)

    # Using part 1 dictionary, count # of a's in the values and set
    #   to the new value.
    food_prefs2 = {k: data.count('a') for k, data in food_prefs.iteritems()}

    print(food_prefs2)

    # Sets s2, s3 and s4 contain #'s from
    #     0 through 20, divisible 2, 3 and 4.
    s2 = {x for x in range(21) if x % 2 == 0}
    s3 = {x for x in range(21) if x % 3 == 0}
    s4 = {x for x in range(21) if x % 4 == 0}

    # Display sets
    print(s2)
    print(s3)
    print(s4)

    # Build a sequence of divisable sets (Extra credit)
    # Test it for 2 through 6
    divisable_sets = [{x for x in range(21) if x % i == 0}
                      for i in (range(2, 7))]

    # Display sets
    print(divisable_sets)
