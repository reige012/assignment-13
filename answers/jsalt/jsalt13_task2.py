#! usr/bin/env python
# encoding: utf-8

"""
Assignment 13
Task 2 Program: Using classes to count words
Jessie Salter
8 March 2016
"""

import argparse
import os
import re
from collections import Counter


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


class Text:
    '''Represents a text file.'''
    def __init__(self, filename):
        with open(filename, 'r') as text:
            self.text = text.read()
        self.filename = filename
        self.path = os.path.abspath(self.filename)

    def __str__(self):
        return self.text

    def total_words(self):
        '''Prints the total number of words in the input file and number of
        unique words.'''
        split_list = re.findall(
                                # Captures words with apostrophes and hyphens:
                                "[a-zA-z]+['][a-zA-Z]+|[a-zA-Z]+|\w+[-]\w+|",
                                self.text)
        full_list = [str.lower(word) for word in split_list]
        # For some reason I'm getting one empty string; this gets rid of it:
        self.all_words = list(filter(None, full_list))
        self.total_words = len(self.all_words)
        unique = len(set(self.all_words))
        print(
            'There are {} words in {}, of which {} are unique.'
            .format(self.total_words, self.filename, unique)
            )
        return self.all_words

    def total_punc(self):
        '''Prints the number of types of punctuation in the input file'''
        self.punc_list = re.findall('[^\s\w]', self.text)
        self.total_punc = len(self.punc_list)
        unique = len(set(self.punc_list))
        print(
            'There are {} types of punctuation in {}.'
            .format(unique, self.filename)
            )

    def word_count(self):
        '''Formats the text by removing capitalization, whitespace, and
        punctuation and storing each word as a separate string in a list.'''
        word_count = Counter(self.all_words)
        return word_count

    def punc_count(self):
        '''Returns a list of each punctuation element found in the text.'''
        punc_count = Counter(self.punc_list)
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


def main():
    args = parser()
    text = Text(args.input)
    text.total_words()
    text.total_punc()
    wc = text.word_count()
    text.pretty_print(wc, args.word_count)
    pc = text.punc_count()
    text.pretty_print(pc, args.punc_count)


if __name__ == '__main__':
    main()
