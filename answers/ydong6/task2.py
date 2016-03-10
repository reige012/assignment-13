#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2016
[ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses `argparse` to get the input filename (1.0 pt)
- [ ] Program uses a class-based approach and includes the requested attributes and methods (4.0 pt)
- [ ] Program correctly counts and displays both words and puncutation in any file (2.0 pt)
@author: York
'''

import argparse
import collections
import os
import re
from collections import Counter


def parser_file_input():
    """Function takes a file as input and ask for a name for output file"""
    parser = argparse.ArgumentParser(
            description="""Input a file to use and an output file name"""
            )
    parser.add_argument(
                '--input',
                required=True,
                type=str,
                help='Enter the name of the file containing text.'
            )
    #parser.add_argument('--output',required=True,type=str,help='Write into new file.')
    return parser.parse_args()


def cleanup(quote):
    cleaned_quote_0 = quote.lower()
    cleaned_quote_1 = cleaned_quote_0.replace(".", "").replace(",", "").replace(";","").replace("'","").replace(")","").replace("(","").replace(":","").replace("!","")
    cleaned_quote_2 = cleaned_quote_1.replace("\n\n", " ")
    return cleaned_quote_2

class Filecounts: 
    def __init__(self, input):
        self.infile = input
        self.filepath = os.path.abspath(self.input)
        self.filename = os.path.basename(self.input)
        with open(input, 'r') as nu:
            self.nu = nu.read()
   
    def path_name(self):
        path = self.filepath
        name = self.filename
        return path, name

    def __str__(self):
        return self.args
    
    
    def punctuations(self):
        puncs = re.findall('[^\s\w]', self.args)
        countedpuncs = Counter(puncs).most_common(10)
        print("\n The punctuation is \n")
        return countedpuncs


def makelist(parsed_quote):
    parsed = parsed_quote.split(" ")
    return parsed


def make_dict(quote_as_list):
    word_count = []
    for word in quote_as_list:
        total = 0
        for item in quote_as_list:
            if word == item:
                total += 1
        word_count.append(total)
    zip_dict = dict(zip(quote_as_list, word_count))
    return zip_dict


def count_lines(zip_dict):
    index=0
    for line in zip_dict:
        line=+1
        index+=1
    print("total number of words in file", index)
    return index


def file_name(new_filename):
    filename=os.path.join("/some/other/path", new_filename)
    print(filename)


def top_twenty_words(the_dict):
    #top_ten = heapq.nlargest(10, the_dict, key=the_dict.get)
    top_twenty_sorted = sorted(the_dict.items(), key=lambda x: (-x[1], x[0]))[:20]
    return top_twenty_sorted


def main():
    args = parser_file_input()
    with open(args.input, 'r') as thats_the_file:
        quote=thats_the_file.read()
        #print(quote)
    cleaned_quote = cleanup(quote)
    #print(cleaned_quote)
    quote_as_list = makelist(cleaned_quote)
    #print(quote_as_list)
    word_count_dict = make_dict(quote_as_list)
    
    print(word_count_dict)
    top_twenty = top_twenty_words(word_count_dict)
    print("\n\nThe twenty most common words in the dictionary and their word counts:\n")
    for item in top_twenty:
        print('%s\t\t%s'%(item[0],item[1]))
    zip_dict=make_dict(quote_as_list)
    count_lines(zip_dict)
    new_filename=("File name")
    file_name(new_filename)
        #print(item[0] + "\t" + str(item[1]))
    print("\n\n")
    #o=args.output
    #counted= write_file(word_count_dict,o)
    #print(counted)
    
if __name__ == '__main__':
    main()