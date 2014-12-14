#!/usr/bin/env python

# count_evens
#
# This module contains one function that returns the number of even
# numbers in a list.


def count_evens(nums):
   return len([x  for x in nums if x % 2 == 0])


if __name__ == '__main__':
    # Test Lists
    l1 = [2, 1, 2, 3, 4]
    l2 = [2, 2, 0]
    l3 = [1, 3, 5]

    assert(count_evens(l1) == 3)
    assert(count_evens(l2) == 3)
    assert(count_evens(l3) == 0)

    print("Passed all asserts.")
