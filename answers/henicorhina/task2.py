# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 11
Oscar Johnson 4 March 2016
"""

import argparse
import collections
import os
import re

def get_args():
    parser = argparse.ArgumentParser(
            description="""takes input file from task 1""")
    parser.add_argument('--file',
                        dest = "file_input",
                        required = True,
                        help = "enter a .txt input file containing counts of words"
                        )
    return parser.parse_args()


class File():
    """
    maniuplation of text files; word count, file name, path, etc.
    """    
    def __init__(self, my_file):
        self.my_file = my_file

    def filename(self):
        """get file name"""
        path = os.path.abspath(self.my_file)
        self.filename = os.path.basename(path) 
        return self.filename
    
    def path(self):
        """get absolute path"""
        self.path = os.path.abspath(self.my_file)
        return self.path

    def word_count(self):
        """get count of words from text file as dictionary Counter"""
        count_all = collections.Counter()
        with open(self.my_file) as my_text:
            for line in my_text:
                text = line.lower() #lowercase all text
                text = re.sub("['-;:()&?!%,]", '', text) #remove non-alphanumeric chars
                text = re.sub("[\n]", '', text) #remove newlines
                text = re.sub('[.]', ' ', text) #replace periods with whitespace
                l = text.split() #listify
                # count of all words
                for word in l:
                    count_all[word] += 1
        self.word_count = len(count_all)
        my_dict = dict(count_all) # convert to regular dictionary
        count_of_words = [] 
        for key, value in my_dict.items():
            # add words and values to list in form of tuples
            count_of_words.append((value, key))
        count_of_words.sort(reverse=True) #sort words in descending abundance
        for value, key in count_of_words[0:20]:
            x = "{:<15}{:^15}".format(key, value)
            print(x)
        return count_all

    def punctuation(self):
        """get all punctuation"""
        count_all = collections.Counter()
        with open(self.my_file) as my_text:
            for line in my_text:
                text = line.lower() #lowercase all text
                text = re.sub('[A-Za-z]', '', text)
                text = re.sub('[0-9]', '', text)
                text = re.sub('[\n]', '', text)
                text = re.sub(' ', '', text)
                for item in text:
                    count_all[item] += 1
                self.punctuation = count_all
        my_dict = dict(count_all) # convert to regular dictionary
        count_of_punct = [] 
        for key, value in my_dict.items():
            # add words and values to list in form of tuples
            count_of_punct.append((value, key))
        count_of_punct.sort(reverse=True) #sort words in descending abundance
        for value, key in count_of_punct[0:10]:
            x = "{:<15}{:^15}".format(key, value)
            print(x)
        return count_all



def main():
    args = get_args()
    my_file = File(args.file_input)
    #print(args, my_file)
    
if __name__ == '__main__':
    main()