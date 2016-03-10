#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 13 Task 2

Amie Settlecowski
10 Mar. 2016

Word-counting class: WordCount.

python task2_settlecowski.py --i input_file.txt --path path\to\directory\of\i\
"""


from collections import Counter
import argparse
import os
import string


def path_arg(parserr):
    ''' requires --path flag for user to indicate path to appropriate directoy'''
    parserr.add_argument("--path",
        required=True,
        help="Path to directory containing this program and input file",
        type=str)


def infile_arg(parserr):
    '''requires --i flag for user to indicate input file name'''
    parserr.add_argument("--i",
        required=True,
        help="Name of input file, including file extension",
        type=str)


class WordCount():
    '''Counts the words and punctuations marks of a file'''
    def __init__(self, in_file):
        '''Requisite attributes'''
        self.file_name = in_file
        self.file_path = os.path.abspath(in_file)
        counts = self.construct_counts(in_file)
        self.word_counts = counts[0]
        self.punct_counts = counts[1]
        self.word_count = len(self.word_counts.keys())
        self.punctuation = list(self.punct_counts.keys())

    def construct_counts(self, in_file):
        ''' Construct 2 Counters of words and punctuation marks'''
        word_counter = Counter()
        punct_counter = Counter()
        # check that input file opens in read mode w/out error
        with open(in_file, 'r') as f:
            if f.readable() == 'False':
                f.close()
            else:
                pass
            for line in f:
                x = self.process_line(line)
                words = x[0]
                puncts = x[1]
                word_counter = self.cnt(words, word_counter)
                punct_counter = self.cnt(puncts, punct_counter)
            f.close()
        return word_counter, punct_counter

    def process_line(self, strng):
        '''
        Parse a string by spaces into 2 lists: words and punctuation marks
        '''
        strng = strng.lower().replace("\r\n", " ")
        new_strng = ''
        punct_list = []
        for character in strng:
            if character in string.punctuation:
                punct_list.append(character)
            if character.isalpha() or character == ' ':
                new_strng += character
        list_of_words = new_strng.split(' ')
        return list_of_words, punct_list

    def cnt(self, lst, cntr):
        '''Populate Counter cntr with occurrences of each item in lst'''
        for item in lst:
            cntr[item] += 1
        return cntr

    def display(self, cntr, rank):
        '''Prints most common keys in a Counter (cntr) and their counts'''
        width = len(max(cntr, key=len))
        rank_counts = cntr.most_common(len(cntr.items()))
        n = 0
        for index in rank_counts:
            if n < rank:
                print('{0:{3}{width}}{2}{1:{3}}'.format(index[0], index[1],
                                                        '\t', '<', width=width))
            n += 1

    def __str__(self,):
        return '{}:\n{} words\n{} punctuation marks'.format(
                self.file_path,
                self.word_count,
                len(self.punctuation))


def main():
    # creater Parser object with arguments for path and input file
    file_name_parser = argparse.ArgumentParser()
    infile_arg(file_name_parser)
    path_arg(file_name_parser)
    file_name_args = file_name_parser.parse_args()
    os.chdir(file_name_args.path)

    # test WordCount class
    print('Testing WordCount class: ''\n''Printing WordCount object:')
    file_counts = WordCount(file_name_args.i)
    print(file_counts)
    print('\n''Displaying 20 most common word counts:')
    file_counts.display(file_counts.word_counts, 20)
    print('\n''Displaying 10 most common punctuation mark counts:')
    file_counts.display(file_counts.punct_counts, 10)

if __name__ == '__main__':
    main()
