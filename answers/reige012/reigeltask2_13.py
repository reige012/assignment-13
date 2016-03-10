#!/usr/bin/env python
# encoding: utf-8

"""
This program creates a class called WordCount() that takes any filepath as
input using argparse and provides some basic information about the filepath
including the filepath, the filename, the total words in the text, the total
punctutation in the text. Then it gives you the counts for the top 20 most
used words and the top 10 most used punctuations.

*Note to user. You must input the whole file path to make this work.
For example your command line should look like:
In: python reigeltask2_13.py --filepath "entire file path"
I find that dragging the file to the command line works best in windows as it
will automatically deposit the entire path.

Edited by Alicia Reigel. 10 March 2016.
Copyright Alicia Reigel. Louisiana State University. 10 March 2016. All
rights reserved.

"""

import argparse
import re
from collections import Counter
import os
import string


class WordCount():
    """a class to do word counts on text"""
    def __init__(self):
        """defines the instance attributes of the WordCount() class"""
        args = self.parser_filepath()
        # runs the parser_filepath to make user give filepath on command line
        self.filename = os.path.basename(args.filepath)
        # uses filepath given to find the file name and set to self.filename
        self.total_words()
        # runs the total words function to count total # of words in text
        self.total_punc_count()

    def parser_filepath(self):
        """Collects the path of the file you want to count words from"""
        parser = argparse.ArgumentParser(
            description="""Input the full path to the file you want to count"""
            )
        parser.add_argument(
                '--filepath',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
        return parser.parse_args()

    def __str__(self):
        """returns the WordCount in a nice format for printing"""
        return "Filepath={}\nFileName={}\nTotal Words={}\nTotal Punctuation:{}".format(self.parser_filepath(), self.filename, self.total_words(), self.total_punc_count())

    def total_words(self):
        """counts the total words in the given file"""
        with open(self.filename, 'r') as the_string:
            all_of_it = the_string.read()
            total_words = len(all_of_it.split(' '))
            return total_words

    def total_punc_count(self):
        """counts the total number of punctuation marks in the given file"""
        with open(self.filename, 'r') as the_string:
            all_text = the_string.read()
            count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
            # thanks stack overflow for this little helper. I know its not ideal, but I can't figure out another solution.
            all_punc = count(all_text, string.punctuation)
            return all_punc

    def word_count(self):
        """cleans up the string, count the words and output the results"""
        with open(self.filename, 'r') as input_data:
            a_string = input_data.read()
            clean_string = a_string.replace('  ', ' ').casefold()
            # substitutes spaces and lowers case
            the_new_list = re.split('\W+', clean_string)
            # splits on spaces to make a list of words
            count_dict = Counter(the_new_list)
            # creates a counted dictionary of all the words
            top_count = count_dict.most_common(20)
            # obtains the top 20 most used words and their counts
            return top_count

    def punctuation_count(self):
        """Counts punctuation and returns the top 10 most used."""
        with open(self.filename, 'r') as input_data:
            a_string = input_data.read()
            count = Counter(c for line in a_string for c in line if c in string.punctuation)
            top_count = count.most_common(10)
            # obtains the top 20 most used words and their counts
            return top_count

    def print_the_counts(self):
        words_count = self.word_count()
        print("These are the top 20 most used words and their counts:")
        for i in words_count:
            print('{}:{}\n'.format(i[0], i[1]))
        punc_count = self.punctuation_count()
        print("These are the top 10 punctuation marks used and their counts:")
        for key, value in punc_count:
            print('{}:{}\n'.format(key, value))


def main():
    words = WordCount()
    print(words)
    words.print_the_counts()


if __name__ == '__main__':
        main()
