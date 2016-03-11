#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to Write a program to count word usage in the text
count the most 20 common words use collection module, and argparser
"""
from collections import Counter
import argparse
from string import punctuation
# import os


class Wordcounting:

    def __init__(self, filename):
        self.filename = filename
        self.read()

    def read(self):
        with open(self.filename, 'r') as infile:
            self.contents = infile.read()

    def count_word(self):
        """
        remove, and change all characters to lower case, count the frequency
        words
        """

        text1 = self.contents.replace(",", " ").replace(".", " ")
        text2 = text1.replace("?", " ").replace("/", " ").replace("!", " ")
        text3 = text2.replace(":", " ").replace(";", " ").casefold()
        text4 = text3.replace(")", " ").replace(" (", " ")
        text5 = text4.replace("  ", " ")
        text6 = text5.split()
        counttext = Counter(text6)
        mostcommon = counttext.most_common(20)
        for i in mostcommon:
            A = "{}{}{}".format(i[0], "\t", i[1])
            print(A)

    def count_punctuation(self):
        c = Counter(c for line in self.contents for c in line if c in
                    punctuation)
        d = c.most_common(10)
        print(d)


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_parser()
    word_counting = Wordcounting(args.inputfile)
    word_counting.count_word()
    word_counting.count_punctuation()


if __name__ == '__main__':
    main()
