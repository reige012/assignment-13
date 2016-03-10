# !/usr/bin/env python
# encoding: utf-8


"""
My word-counting program
Created by Andre Moncrieff on 1 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import argparse
from collections import Counter
import os


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", required=True,
                        help="Enter '--input_file', space, and then" +
                        " the name of the input file.", type=str)
    args = parser.parse_args()
    return args


class WordCounter:
    def __init__(self,
                 filename,
                 file_object,
                 ):
        self.file_name = os.path.basename(filename)
        self.file_path = os.path.abspath(filename)
        self.file_object = file_object
        # self.total_word_count = total_word_count
        # self.all_punc_types_used=all_punc_types_used

    def cleaned_up_word_list(self):
        word_list = []
        punctuation = set("(),.?/!;:'\n\t")
        for line in self.file_object:
            if line != "\n":
                cleaned_line_0 = "".join(c for c in line if c not in
                                         punctuation)
                cleaned_line_1 = cleaned_line_0.casefold()
                parsed = cleaned_line_1.split(" ")
                word_list.extend(parsed)
        return word_list

    def word_count(self, word_list):
        total_word_count = len(word_list)
        WordCounter.total_word_count = total_word_count
        return self.total_word_count

    def cleaned_up_punct_list(self):
        punct_list = []
        letters_numbers = set(" \n\tABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        for line in self.file_object:
            if line != "\n":
                cleaned_line = "".join(c for c in line if c not in
                                         letters_numbers)
                parsed = cleaned_line.split(" ")
                punct_list.extend(parsed)
        indiv_punct_list = []
        for item in punct_list:
            indiv_punct_list.extend(item)
        return indiv_punct_list

    def set_of_punct(self, punct_list):
        punct_set = set(punct_list)
        WordCounter.punct_set = punct_set
        return self.punct_set

    def count_and_dictionate(self, word_list):
        word_count_dict = Counter(word_list)
        WordCounter.word_count_dict = word_count_dict
        return self.word_count_dict

    def top_words(self, dictionary):
        top_twenty = dictionary.most_common(20)
        WordCounter.top_twenty = top_twenty
        return self.top_twenty

    def top_punct(self, dictionary):
        top_ten = dictionary.most_common(10)
        WordCounter.top_ten = top_ten
        return self.top_ten

    def display(self, word_number_dict):
        for item in word_number_dict:
            if len(item[0]) < 8:
                print("{}{}{}".format(item[0], "\t\t", item[1]))
            if len(item[0]) >= 8:
                print("{}{}{}".format(item[0], "\t", item[1]))
        print("{}".format("\n\n"))





def main():
    args = parser()
    file_object = open(args.input_file, "r")

    doc_word = WordCounter(args.input_file, file_object)
    #print("The file name of the input file is: ", doc_word.file_name)
    #print("The file path of the input file is: ", doc_word.file_path)
    word_list = doc_word.cleaned_up_word_list()
    doc_word.word_count(word_list)
    #print("The total number of words in the file is: ", doc_word.total_word_count)
    doc_word.count_and_dictionate(word_list)
    doc_word.top_words(doc_word.word_count_dict)
    print("\n\nThe top twenty words and their counts:\n")
    doc_word.display(doc_word.top_twenty)

    file_object.close()
    file_object = open(args.input_file, "r")

    doc_punct = WordCounter(args.input_file, file_object)
    indiv_punct_list = doc_punct.cleaned_up_punct_list()
    doc_punct.count_and_dictionate(indiv_punct_list)
    doc_punct.set_of_punct(indiv_punct_list)
    #print("Types of punctuation used in file: ", doc_punct.punct_set, "\n\n")
    doc_punct.top_punct(doc_punct.word_count_dict)
    print("The top ten punctuation types and their counts:\n")
    doc_punct.display(doc_punct.top_ten)

    file_object.close()



if __name__ == '__main__':
    main()
