#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
10 March 2016
Assignment 13 Task 2

A program with a new class WordCounter that takes a file as input and returns
the counts of each words, and the counts of punctuation.

This program doesn't work!!!
'''
import argparse
import string
from collections import Counter
import os


class WordCounter():
    '''doesn't work'''
    def __init__(self):
        args = self.get_args()
        self.args = args
        self.get_filenames(args)
        filename = os.path.basename(args.infile)
        self.directory = os.path.split(args.infile)[0]
        # self.filename = filename
        # self.directory = directory

    def __str__(self, word, vale, filename, directory):
        return ("The punctuation is: {0:15}{1}\n".format(self.word, self.value))
        return ("The word count is: {0:15}{1}\n".format(self.word, self.value))
        return ("The file is {}, The path is {}".format(self.filename,
                                                        self.directory))

    def get_filenames(self, args):
        self.filename = os.path.basename(args.infile)
        self.directory = os.path.split(args.infile)[0]

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--infile",
            required=True,
            help="""The input file name"""
        )
        return parser.parse_args()

    def histogram(self, args):
        exclude = set(string.punctuation)
        with open(self.args.infile, 'r') as f:
            my_input = f.read()
            remove_ch = ''.join(ch for ch in my_input if ch not in exclude)
            make_list = remove_ch.lower().replace('\n', ' ').split(' ')
            count = Counter(make_list)
            for val, freq in count.most_common(20):
                return val, freq

    def punct_count(self, args):
        include = set(string.punctuation)
        with open(self.args.infile, 'r') as f:
            my_input = f.read()
            remove_ch = ''.join(ch for ch in my_input if ch in include)
            make_list = remove_ch.replace('\n', ' ').split(' ')
            count = Counter(make_list)
            for val, freq in count.most_common(10):
                return val, freq


def main():
    hist = WordCounter()
    count_words = hist.histogram(args)
    print(count_words)
    count_punct = hist.punct_count(args)


if __name__ == '__main__':
    main()
