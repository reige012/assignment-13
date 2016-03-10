#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 13, Task 2
Austen T. Webber
2016_3_10
"""


import os
import string
import argparse
import re
from collections import Counter


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Input file:")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide an input file as -- 'file'",
        type=str
    )
    return parser.parse_args()


class Counting:
    def __init__(self, inputfile):
        self.inputfile = inputfile
        self.basename = os.path.basename(self.inputfile)
        self.filepath = os.path.abspath(self.inputfile)
        self.word_totalcount()
        self.punct_totalcount()

    def printing(self):
        x = self.filepath
        y = self.inputfile
        return x, y

    def word_totalcount(self):
        with open(self.inputfile, "r") as string:
            string = string.read()
            counters = len(string.split())
            print(counters)

    def punct_totalcount(self):
        with open(self.inputfile, "r") as fun:
            funner = fun.read()
            count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
            counters = count(funner, string.punctuation)
            print(counters)

    def word_count(self):
        with open(self.inputfile, "r") as string:
            string = string.read()
            list = re.split('\W+', string)
            my_dict = [str.lower(word) for word in list]
            numbers = Counter(my_dict).most_common(20)
        return numbers

    def punct_count(self):
        with open(self.inputfile, "r") as string:
            string = string.read()
            my_dict = string.replace(" ", "").replace("  ", "").replace("\n", "").strip()
            list = re.split('\w+', my_dict)
            numbers = Counter(list).most_common(10)
        return numbers

def main():
    userinput = askingforfiles()
    vols = Counting(userinput.input)
    vol = vols.printing()
    print("Path to file: r\n", vol)
    counts = vols.word_count()
    print("Count of input file: r\n")
    for item in counts:
        print("{} {}".format(item[1], item[0]))
    punct = vols.punct_count()
    print("Count of punctuation: \r\n")
    for item in punct:
        print("{} {}".format(item[1], item[0]))


if __name__ == '__main__':
    main()

# https://docs.python.org/2/library/re.html
# http://stackoverflow.com/questions/21852066/counting-word-frequency-and-making-a-dictionary-from-it
