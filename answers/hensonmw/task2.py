#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 13

Created by Michael Henson on 09 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""
import argparse
import os
import re
from collections import Counter
import string

def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking User to Provide a input file ")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide the output file from task1",
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
            #https://docs.python.org/2/library/re.html
            '''
            this took me forever to figure out and what to use
            since I previous got this wrong. this seems simple compared
            to previous attempted to break apart using string
            '''
            '''
            http://stackoverflow.com/questions/10134372/get-a-list-of-names-which-start-with-certain-letters
            First answer helped tell me how to put together a list comprehension.
            '''
            my_dict = [str.lower(word) for word in list]
            numbers = Counter(my_dict).most_common(20)
        return numbers

    def punct_count(self):
        with open(self.inputfile, "r") as string:
            string = string.read()
            my_dict = string.replace(" ", "").replace("  ", "").replace("\n", "").strip()
            list = re.split('\w+', my_dict)
            #https://docs.python.org/2/library/re.html
            '''
            this took me forever to figure out and what to use
            since I previous got this wrong. this seems simple compared
            to previous attempted to break apart using string
            '''
            '''
            http://stackoverflow.com/questions/10134372/get-a-list-of-names-which-start-with-certain-letters
            First answer helped tell me how to put together a list comprehension.
            '''
            numbers = Counter(list).most_common(10)
        return numbers

def main():
    userinput = askingforfiles()
    xxx = Counting(userinput.input)
    xx = xxx.printing()
    print("What is my path to my file and its base name kind sir? \n", xx)
    counts = xxx.word_count()
    print("What is the total count of my input file \n")
    for item in counts:
        print("{} {}".format(item[1], item[0]))
    punct = xxx.punct_count()
    print("\nWhat is the total count of my input file \n")
    for item in punct:
        print("{} {}".format(item[1], item[0]))





if __name__ == '__main__':
    main()
