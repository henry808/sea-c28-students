#!/usr/bin/env python

# Define the original list
fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]


if __name__ == '__main__':

    # First series of actions:
    print(fruit_list)
    fruit = unicode(raw_input(u"Enter a new fruit: "))
    fruit_list.append(fruit)
    print(fruit_list)
    index = int(
        raw_input(u"Enter a number for the position of the fruit you want: "))

    if index > 0 and index <= len(fruit_list):
        print(u"The fruit in the %i position is %s" %
            (index, fruit_list[index - 1]))
    else:
        print(u"Position out of range.")

    fruit_list = [u"Banana"] + fruit_list
    print(fruit_list)
    fruit_list.insert(0, u"Lime")
    print(fruit_list)

    for fruit in fruit_list:
        if(fruit[0] == u"P"):
            print(fruit)
    print("")

    # Second series of actions:
    # fruit_list2 = fruit_list[:]
    # print(fruit_list2)
    # del fruit_list2[-1:]
    # print(fruit_list2)
    # fruit = unicode(raw_input(u"Enter a fruit to delete: "))
    # fruit_list2.remove(fruit)
    # print(fruit_list2)
    # print("")

    # Third series of actions:
    # fruit_list3 = fruit_list[:]
    # print(fruit_list3)
    # for fruit in fruit_list:
    #     while True:
    #         like = unicode(raw_input(u"Do you like %s? " % fruit))
    #         if like == u"no":
    #             fruit_list3.remove(fruit)
    #             break
    #         elif like == u"yes":
    #             break
    # print(fruit_list3)
    # print("")

    # Fourth series of actions:
    fruit_list4 = fruit_list[:]
    for i in range(len(fruit_list4)):
        fruit_list4[i] = fruit_list4[i][::-1]

    print(fruit_list4)
    fruit_list.pop()
    print(fruit_list)