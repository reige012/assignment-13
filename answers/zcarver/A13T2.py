#! /usr/bin/env python
# encoding UTF-8

'''
Assignment13Task2 biol7800
ZacCarver 03/10/2016
'''

import argparse
import os
import re
from collections import Counter


class Filecounts:

    def __init__(self, infile):
        self.infile = infile
        self.filepath = os.path.abspath(self.infile)
        self.filename = os.path.basename(self.infile)
        with open(infile, 'r') as f:
            self.f = f.read()

    def __str__(self):
        return self.f

    def path_name(self):
        path = self.filepath
        name = self.filename
        return path, name
    '''
    def totalwords(self):
        fw = self.f
        tw = len(fw.split())
        print("total words: ", tw)
    '''

    def wordcount(self):
        words = re.split('\W+', self.f)
        wldict = [str.lower(word) for word in words]
        countedwords = Counter(wldict).most_common(20)
        print("Your File's Top 20 words \n")
        return countedwords

    def punctuations(self):
        puncs = re.findall('[^\s\w]', self.f)
        countedpuncs = Counter(puncs).most_common(10)
        print("\n Your File's Punctuations \n")
        return countedpuncs


def args():
    parser = argparse.ArgumentParser(description='''task1 product file in''')
    parser.add_argument("--infile", type=str, help='enter file')
    return parser.parse_args()


def main():
    arg = args()
    f = Filecounts(arg.infile)
    countedwords = f.wordcount()
    for item in countedwords:
        print('{} {}'.format(item[1], item[0]))
    countedpuncs = f.punctuations()
    for item in countedpuncs:
        print('{} {}'.format(item[1], item[0]))

if __name__ == '__main__':
    main()
