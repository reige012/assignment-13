#!/usr/bin/env python
# utf-8

"""
Task2 of assignment 13.
most common words.
Created by Pramod Pantha on 10 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import argparse
import collections
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


class Counter:
    def __init__(self, inputfilename, file_object):
        self.inputfilename = inputfilename
        self.filepath = os.path.basename(self.inputfilename)
        self.filepath = os.path.abspath(self.inputfilename)
        self.file_object = file_object

    def edited_word_list(self):
        line_list = []
        punctuation = set("(),.?/!;:'\n\t")
        for line in self.file_object:
            if line != "\n":
                cleaned_line_0 = "".join(c for c in line if c not in punctuation)
                cleaned_line_1 = cleaned_line_0.casefold()
                parsed = cleaned_line_1.split(" ")
                line_list.extend(parsed)
            return line_list

    def word_count(self, line_list):
        total_word_count = len(line_list)
        Counter.total_word_count = total_word_count
        return self.total_word_count

    def edited_punct_list(self):
        punct_list = []
        letters_numbers = set(" \n\tABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        for line in self.file_object:
            if line != "\n":
                edited_line = "".join(c for c in line if c not in
                                      letters_numbers)
                parsed = edited_line.split(" ")
                punct_list.extend(parsed)
        indiv_punct_list = []
        for item in punct_list:
            indiv_punct_list.extend(item)
        return indiv_punct_list

    def collection_punct(self, list_punct):
        punct_set = set(list_punct)
        Counter.punct_set = punct_set
        return self.punct_set

    def count_and_dictionate(self, line_list):
        word_count_dict = Counter(line_list)
        Counter.word_count_dict = word_count_dict
        return self.word_count_dict

    def top_words(self, the_dict):
        # gives top 20 most frequent words
        top20 = the_dict.most_common(20)
        Counter.top20 = top20
        return self.top20

    def top_punct(self, the_dict):
        # gives top 10 most frequent punctuation
        top10 = the_dict.most_common(10)
        Counter.top10 = top10
        return self.top10

    def file_writer(self, word_count_dict, output_file):
        sorted_dict = sorted(word_count_dict.items(), key=lambda x: (-x[1], x[0]))
        # print("sorted_dict: ", sorted_dict)
        for item in sorted_dict:
            if len(item[0]) < 8:
                # print(len(item))
                output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))
            if len(item[0]) >= 8 and len(item[0]) < 16:
                output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))
            if len(item[0]) >= 16:
                output_file.write("{}{}{}{}".format(item[0], "\t", item[1], "\n"))


def main():
    args = parser()
    file_object = open(args.input_file, "r")
    doc_word = Counter(args.input_file, file_object)
    word_list = doc_word.edited_word_list()
    doc_word.word_count(word_list)
    doc_word.count_and_dictionate(word_list)
    doc_word.top_words(doc_word.word_count_dict)
    print("\n\nTop twenty words and their counts for epigenic chapter:\n")
    doc_word.display(doc_word.top_twenty)
    file_object.close()
    file_object = open(args.input_file, "r")
    doc_punct = Counter(args.input_file, file_object)
    indiv_punct_list = doc_punct.cleaned_up_punct_list()
    doc_punct.count_and_dictionate(indiv_punct_list)
    doc_punct.set_of_punct(indiv_punct_list)
    doc_punct.top_punct(doc_punct.word_count_dict)
    print("Top ten punctuation types and their counts for epigenetic chapter:\n")
    doc_punct.display(doc_punct.top_ten)
    file_object.close()


if __name__ == '__main__':
    main()
