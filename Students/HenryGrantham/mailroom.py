#!/usr/bin/env python

# Mailroom
#
# Sets up and sends out emails to doners.


def printlist():
    """Print a list of donor names
    """
    for donorinfolist in donorlist:
        print(donorinfolist[0])


def addnametolist(name):
    """Add a name to the list
    """
    donorlist.append([name])


def addamounttolist(name, amount):
    """Add amount to the list of amounts for a donor
    """
    for currentname in donorlist:
        if currentname[0] == name:
            currentname[1].append(amount)


def generateemail(donor):
    """Print email to terminal
    """
    donations = ", ".join(donor[1])
    print(u"Thank you, %s for your generous donations of %s."
          % donor[0], donations)
    # Fix this to take multiple arguments


def sendthankyou():
    """Takes steps to add donor or email thank you.
    """
    quiting = False  # if user quits, set this to True
    while not(quiting):
        donorname = unicode(raw_input(u"""What is the donor's name?
        (type quit to exit to menu)"""))
        if donorname == 'quit':
            quiting = True
        elif donorname in donorlist:
            break
        elif len(donorname) > 0:
            addnametolist(donorname)
            break
        else:
            continue

    while not(quiting):
        donoramount = unicode(raw_input(u"""How much did they donate?
        (type quit to exit to menu)"""))
        if donoramount == 'quit':
            quiting = True
        elif donoramount.isnumeric():
            addamounttolist(donorname, donoramount)
            generateemail(donorname)
            break
        else:
            continue


def createreport():
    """Create a report with list of donors and amounts they donated.
    """
    pass
    #sort on amount

if __name__ == '__main__':

    # I got ahead of myself here.
    #
    # Save this assignment for later.
    # donordict = {'Will Jorg': (20, 10, 30),
    #              'Jim MCCaine': (11, 22),
    #              'Sally James': (200, 40),
    #              'Jill Kim': (35, 67),
    #              'Anthony Wong': (100)
    #              }

    donorlist = [['Will Jorg', [20, 10, 30]],
                 ['Jim MCCaine', [11, 22]],
                 ['Sally James', [200, 40]],
                 ['Jill Kim', [35, 67]],
                 ['Anthony Wong', [100]]]

    # Menu with three choices
    while True:
        choice = unicode(raw_input(u"""
        1 Send a Thank You\n
        2 Create a Report\n
        3 Quit\n
        Please choose 1,2, or 3:"""))
        if choice == '1':
            sendthankyou()
        elif choice == '2':
            createreport()
        elif choice == '3':
            break
        else:
            pass
    printlist()
