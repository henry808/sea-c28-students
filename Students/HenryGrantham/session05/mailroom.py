#!/usr/bin/env python

# Mailroom
#
# Maintains a list of donors and sends out emails to them.
from collections import OrderedDict


def printlist(ddict):
    """Print a list of donor names
    """
    for donor in ddict:
        print(donor)


def addamounttolist(ddict, name, amount):
    """Add amount to the end of a list of amounts for a donor
    """
    ddict[name].append(amount)


def generateemail(ddict, donor):
    """Print email to terminal

    Store an email in symbol email and print it to the screen
    """
    email = "Hi %s,\nThank you for your generous donation of %.2f\n\n" \
            "Thanks,\nGoodbye\n\n" \
            % (donor, ddict[donor][-1])
    print(email)


def sendthankyou(donordict):
    """Takes steps to add donor or email thank you.

    This does two things:
    1) Prompts uses for a name.
    If user puts in a name, it will either add the name into the donor list
    or if the person is already in the list, it will select that donor.
    The name has to be a mix of letters and spaces.
    If user selects list, it will print out a list of names already in.
    If user selects q, it will quit out to main menu.

    2) Prompts user for an amount
    If the user puts in an illegal value (not convertable to a float),
    tell them it is illegal and then reprompt
    If user selects q, it will quit out to main menu. If it is a new donor,
    and they quit, the donor will have an empty list of donation amounts.
    If the value is legal then print an email.
    """

    quiting = False  # if user quits, set this to True
    while not(quiting):
        promptstr = u"What is the donor's name (list for list; q for menu)?"
        donor = unicode(raw_input(promptstr))
        if donor == u'q':
            quiting = True
        elif donor == u'list':
            printlist(donordict)
            continue
        elif donor.replace(' ', '').isalpha():
            donordict.setdefault(donor, [])
            break

    # Add amount to the donating person's donation list.
    while not(quiting):
        promptstr = u"How much did they donate (q to exit to menu)?"
        try:
            donoramount = unicode(raw_input(promptstr))
            if donoramount == u'q':
                quiting = True
            else:
                addamounttolist(donordict, donor, float(donoramount))
                generateemail(donordict, donor)
                break
        except ValueError:
            print(u"Illegal value. Please enter in a number.")
            continue

def createreport(donordict):
    """Create a report with list of donors and amounts they donated.

    Table contains these four columns:
    Donor Name,
    total donated,
    number of donations,
    average donation

    and is sorted by total donations.

    The first column will scale to the size of the donor's name.
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
    longestname = max(len(donor) for donor in donordict)
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
                 u'Anthony Wong': [100.00]
                 }

    # Menu with three choices
    while True:
        choice = unicode(raw_input(
            u"Main Menu\n"
            u"1 Send a Thank You\n"
            u"2 Create a Report\n"
            u"Please choose 1,2, or q to quit:"))
        if choice == '1':
            sendthankyou(donordict)
        elif choice == '2':
            createreport(donordict)
        elif choice == 'q':
            print('Thank you for using mailroom.')
            break
        else:
            pass
