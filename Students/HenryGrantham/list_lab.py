#!/usr/bin/env python

fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]


if __name__ == '__main__':
    print(fruit_list)
    fruit = unicode(raw_input(u"Enter a new fruit: "))
    fruit_list.append(fruit)
    print(fruit_list)
    index = int(raw_input(u"Enter a number for the position of the fruit you want: "))

    if index > 0 and index <= len(fruit_list):
        print(u"The fruit in the %i position is %s" % (index, fruit_list[index - 1]))
    else:
        print(u"Position out of range.")

    fruit_list = [u"Banana"] + fruit_list
    print(fruit_list)
    fruit_list.insert(0, u"Lime")
    print(fruit_list)


