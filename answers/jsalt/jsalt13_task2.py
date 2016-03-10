#! usr/bin/env python
# encoding: utf-8

"""
Assignment 13
Task 2 Program: Using classes to count words
Jessie Salter
8 March 2016
"""

import os
import re
from collections import Counter
import argparse


class Text:
    '''Represents a text file.'''
    def __init__(self, filename):
        self.filename = filename
        self.path = os.path.abspath(self.filename)
        with open(filename, 'r') as text:
            self.text = text.read()

    def __str__(self):
        return self.text

    def word_count(self):
        '''Formats the text by removing capitalization, whitespace, and
        punctuation and storing each word as a separate string in a list.'''
        split_list = re.findall(
                                # Captures words with apostrophes and hyphens:
                                "[a-zA-z]+['][a-zA-Z]+|[a-zA-Z]+|\w+[-]\w+|",
                                self.text)
        full_list = [str.lower(word) for word in split_list]
        # For some reason I'm getting one empty string; this gets rid of it:
        word_list = filter(None, full_list)
        word_count = Counter(word_list)
        return word_count

    def punc_count(self):
        '''Returns a list of each punctuation element found in the text.'''
        punc_list = re.findall('[^\s\w]', self.text)
        punc_count = Counter(punc_list)
        return punc_count

    def pretty_print(self, result, num):
        '''Prints the top number of specified results of word_count or
        punc_count in two-column format.'''
        wc_list = []
        for word, count in result.items():
            wc_list.append([count, word])
            final_list = sorted(wc_list, reverse=True)
        for item in final_list[:num]:
            print('{1:<12}{0:<3}'.format(item[0], item[1]))


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the names of input file.'''
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the name of the input file you would like to work with.",
        type=str
    )
    parser.add_argument(
        "--word_count",
        required=True,
        help="How many of the most common words you want to print.",
        type=int
    )
    parser.add_argument(
        "--punc_count",
        required=True,
        help="How many of the most common punctuation you want to print.",
        type=int
    )
    return parser.parse_args()


def main():
    args = parser()
    text = Text(args.input)
    wc = text.word_count()
    text.pretty_print(wc, args.word_count)
    pc = text.punc_count()
    text.pretty_print(pc, args.punc_count)


if __name__ == '__main__':
    main()
