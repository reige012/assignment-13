#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 13

Created by Michael Henson on 09 March 2016.
With the gracious help of AJ "Da Boss Man" Turner
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
        self.punct_type()

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


    def punct_type(self):
        with open(self.inputfile, "r") as myfile:
            myfiles = myfile.read()
            list2 = string.punctuation
            my_dict = {}
            for punct in list2:
                a = myfiles.count(punct)
                if a > 0:
                    my_dict[punct] = a
                    myfile.close()
            print("\nTypes of punctuation in file:")
            for punct in my_dict:
                print(punct)



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
        with open(self.inputfile, "r") as myfile:
            myfiles = myfile.read()
            list2 = string.punctuation
            my_dict = {}
            for punct in list2:
                a = myfiles.count(punct)
                if a > 0:
                    my_dict[punct] = a
                    myfile.close()
        return sorted(my_dict.items(), key=lambda item: -item[1])[0:10]


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
