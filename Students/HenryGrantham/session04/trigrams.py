#!/usr/bin/env python

# trigrams.py
#
# Create trigrams.


if __name__ == '__main__':
    import codecs
    f = codecs.open('sherlock_small.txt')
    text_data = f.read()
    f.close()

    print(text_data)