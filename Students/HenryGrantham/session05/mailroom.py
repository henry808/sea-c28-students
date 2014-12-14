#!/usr/bin/env python

# Mailroom
#
# Sets up and sends out emails to doners.
from collections import OrderedDict


def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def printlist():
    """Print a list of donor names
    """
    for donor in donordict.keys():
        print(donor)


def addnametolist(name):
    """Add a name to the list
    """
    donordict[name] = []


def addamounttolist(name, amount):
    """Add amount to the list of amounts for a donor
    """
    donordict[name].append(amount)


def generateemail(donor):
    """Print email to terminal
    """
    email = "Hi %s,\nThank you for your generous donation of %.2f\n\n" \
            "Thanks,\nGoodbye\n\n" \
            % (donor, donordict[donor][-1])
    print(email)


def sendthankyou():
    """Takes steps to add donor or email thank you.
    """
    quiting = False  # if user quits, set this to True
    while not(quiting):
        promptstr = u"What is the donor's name (list for list; q for menu)?"
        donor = unicode(raw_input(promptstr))
        if donor == u'q':
            quiting = True
        elif donor == u'list':
            printlist()
            continue
        elif donor in donordict:
            break
        elif donor.replace(' ', '').isalpha():
            addnametolist(donor)
            break
        else:
            continue

    # print(donordict)

    # Add amount to the donating person's donation list.
    while not(quiting):
        promptstr = u"How much did they donate (q to exit to menu)?"
        donoramount = unicode(raw_input(promptstr))
        if donoramount == u'q':
            quiting = True
        elif isfloat(donoramount):
            addamounttolist(donor, float(donoramount))
            generateemail(donor)
            break
        else:
            continue
    # print(donordict)


def createreport():
    """Create a report with list of donors and amounts they donated.

    Table contains these four columns:
    Donor Name,
    total donated,
    number of donations,
    average donation

    and is sorted by total donations.
    """
    # create a sorted donordict sorted by total of amounts.
    sort = sorted(donordict.items(), key=lambda t: sum(t[1]))
    sorteddonorlist = OrderedDict(sort)

    # Columns
    col1 = 'Donor Name'
    col2 = 'Total Donations'
    col3 = '# of Donations'
    col4 = 'Average Donations'

    # determine width of first column
    longestname = max(len(donor) for donor in donordict.keys())
    col1width = max(len(col1), longestname) + 1

    report = "{:{width}} | {:^17} | {:^16} | {:^19}\n"\
        .format(col1, col2, col3, col4, width=col1width)
    for donor in sorteddonorlist:
        col1 = donor
        col2 = sum(sorteddonorlist[donor])
        col3 = len(sorteddonorlist[donor])
        # Prevent divide by zero errors
        try:
            col4 = col2/col3    # average
        except ZeroDivisionError:
            col4 = 0
        report += "{:{width}} | {:>17.2f} | {:>16.2f} | {:>19.2f}\n"\
            .format(col1, col2, col3, col4, width=col1width)
    print(report)


if __name__ == '__main__':

    # Donorlist is a global dict containing a name as a key and
    #      a list of donation amounts as the value
    donordict = {u'Will Jorg': [20.00, 10.00, 30.00],
                 u'Jim MCCaine': [11.50, 22.76],
                 u'Sally James': [200.00, 40.00],
                 u'Jill Kim': [35.00, 67.00],
                 u'Anthony Wong Zinb': [100.00]
                 }

    # Menu with three choices
    while True:
        choice = unicode(raw_input(
            u"1 Send a Thank You\n"
            u"2 Create a Report\n"
            u"Please choose 1,2, or q to quit:"))
        if choice == '1':
            sendthankyou()
        elif choice == '2':
            createreport()
        elif choice == 'q':
            print('Thank you for using mailroom.')
            break
        else:
            pass
