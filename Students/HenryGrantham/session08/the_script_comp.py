#!/usr/bin/env python

# the_script_comp.py
#
# This module contains a function that strips the begining and end of a text
# string and has a script that utilizes it to create a new file or save
# the string over the old file.
import sys
import codecs


def savefile(filestr, text):
    """Saves text to a file at filename and closes the file.
    """
    f = open(filestr, 'w')
    f.write(text)
    f.close()


def cleantext(text):
    """Cleans text of leading and trailing spaces
    """
    if isinstance(text, str):
        str_list = text.split('\n')
        return '\n'.join([t.strip() for t in str_list])
    else:
        raise TypeError("Object is not a string and is type %s" % type(text))


if __name__ == '__main__':
    # read in file and put into text_data
    filename = sys.argv[1]
    f = codecs.open(filename)
    text_data = f.read()
    f.close()

    text_data = cleantext(text_data)

    print(u"Your file has been cleaned of leading"
          u" and trailing spaces.\n\n")

    # Main loop that prompt where you can either save over the old
    # file or save to a new file.
    # Checks for IOError and reprompts for new filename if error.
    while True:
        promptstr = (u"Would you like to:\n"
                     u"1 Save over the same file\n"
                     u"2 Write to a new file\n"
                     u"(list for list; q for menu)?")
        choice = unicode(raw_input(promptstr))
        if choice == '1':
            # save over old file
            savefile(filename, text_data)
            print(u"File has been saved.")
            break
        elif choice == '2':
            # prompt for and save to new filename
            while True:
                try:
                    promptstr = u"Please choose a filename:"
                    filename = unicode(raw_input(promptstr))
                    savefile(filename, text_data)
                    print(u"File has been saved to %s." % filename)
                    break
                except IOError:
                    print(u"Illegal filename. Try again.")
                    continue
            break
        elif choice == 'q':
            # quit without saving
            print(u'You have quit without saving.\n')
            break
        else:
            pass
    print(u'Thank you for using file cleaner.')
