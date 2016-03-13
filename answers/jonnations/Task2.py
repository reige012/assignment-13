#!/usr/bin/env python
# utf-8

"""
Assignment 13, Task 2
Jon Nations on 9 March 2016
Creates a class called Word that counts words and punctuation in ANY text file.

"""

import argparse
from collections import Counter
import re


class Word:

    def __init__(self, args=1):
        self.args = args

    def file_in(self):
        # Does the argparse thing
        parser = argparse.ArgumentParser()
        parser.add_argument('--input', required=True, type=str, help="give input file")
        self.args = parser.parse_args()
        return self.args

    def words(self, args):
        # cleans up txt, leaves only words, and creates a dictionary
        with open(self.args.input, 'r') as in_file:
            clean = in_file.read().lower()
            clean = re.sub('\s+', ' ', clean)
            # condense all whitespace
            clean = re.sub('[^A-Za-z ]+', '', clean)  # remove non-alpha chars
            # regular expressions from gist.github.com/bradmontgomery
            clean_file = clean.split()
            word_dict = {}
            for item in clean_file:
                word_dict[item] = clean_file.count(item)
            return word_dict

    def order_word(self, w_dict, n=20):
        # sorts the dictionary by occurances, then prints
        # the top 20 most-used words
        word_count = Counter(w_dict)
        print("The Top {0} words".format(n))
        for word, count in word_count.most_common(n):
            print("{:<9s}{:>9d}".format(word, count))

    def punct(self, args):
        # cleans up txt, leaves only punctuation, and creates a dictionary
        with open(self.args.input, 'r') as punct_file:
            fresh = punct_file.read()
            fresh = re.sub('\s+', ' ', fresh)  # condense all whitespace
            fresh = re.sub('(''[A-Za-z0-9])', '', fresh)
            # remove all alphanumeric, leaves only punctuation
            fresh_file = fresh.split()
            punct_dict = {}
            for item in fresh_file:
                punct_dict[item] = fresh_file.count(item)
            return punct_dict

    def order_punct(self, p_dict, n=10):
        # sorts the dictionary by occurances, then prints
        # the top 10 most-used punctuations
        punct_count = Counter(p_dict)
        print("The Top {0} Punctuations".format(n))
        for word, count in punct_count.most_common(n):
            print("{:<9s}{:>9d}".format(word, count))


def main():
    word = Word()
    args = word.file_in()
    word.words(args)
    w_dict = word.words(args)
    word.order_word(w_dict)
    word.punct(args)
    p_dict = word.punct(args)
    word.order_punct(p_dict)


if __name__ == '__main__':
    main()
