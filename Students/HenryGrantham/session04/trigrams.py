#!/usr/bin/env python

# trigrams.py
#
# Create trigrams.
import codecs
import string
import random
from string import maketrans

if __name__ == '__main__':
    f = codecs.open('sherlock_small.txt')
    text_data = f.read()
    f.close()

    # Strip out all punctuation and replace with spaces.
    table = maketrans(string.punctuation,
                      "                                ")
    text_data = text_data.translate(table)
    # Make all words smallcase
    text_data = text_data.lower()
    # Make into a list of words
    strlist = text_data.split()

    # build trigramtable: a dictionary of all trigrams with lists of words
    trigramtable = {}
    for i in range(len(strlist)-2):
        k = "%s %s" % (strlist[i], strlist[i + 1])
        word = strlist[i + 2]
        if k in trigramtable.keys():
            trigramtable[k].append(word)
        else:
            trigramtable[k] = [word]

    # Generating new text
    for i in range(200):
        if i == 0:
            # generate starting pair of words by picking random key
            r = random.randint(0, len(trigramtable) - 1)
            text_string = random.choice(list(trigramtable.keys()))
            text_string = text_string.split()
        else:
            if len(text_string) <= i:
                k = "%s %s" % (text_string[i - 2], text_string[i - 1])
                if k in trigramtable.keys():
                    text_string.append(random.choice(trigramtable[k]))
                else:
                    # key does not exist put a '.' on the end and
                    # then generate a new key to start from
                    text_string.append('.')
                    words = random.choice(list(trigramtable.keys()))
                    words = words.split()
                    text_string.append(words[0])
                    text_string.append(words[1])
    # Throw a '.' on the end if there is not one there already.
    if text_string[-1] == '.':
        pass
    else:
        text_string.append('.')

    # Capitalize all I's
    for i in range(len(text_string)):
        if text_string[i] == 'i':
            text_string[i] = 'I'

    # Turn the list of words into sentences
    text_string = " ".join(text_string)
    text_string = text_string.replace(" .", ".")

    print(text_string)
