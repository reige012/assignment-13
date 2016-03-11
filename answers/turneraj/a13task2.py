#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 13. Task includes an object-oriented approach to summarizing word counts for any file type. Attributes included in the object are file name, file path, total words in file, and the type of punctuation in the file. Methods included in the object count words, count punctuation, and display of the results. 

 Created by A.J. Turner on March 9, 2016. Helpful instructions/hints provided by Mikey Henson and S. Shakya.
 Copyright 2016 A.J. Turner. All rights reserved.

"""

import argparse
import os
import re
from collections import Counter
import string

def user_input():
	""" adding user input that includes the name of the file to read and the name of the output file they write"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--file_in", help="Type into command line: --file_in <file name you wish to read>", type=str)
	args = parser.parse_args()
	return args


class Countme:
	""" class object to summarize word counts on a file """
	
	def __init__(self, file_in):
		self.file_in = file_in
		self.basename = os.path.basename(self.file_in)
		self.filepath = os.path.abspath(self.file_in)
		self.total_word()
		self.type_punct()
		self.print_type_punct()

	def file_info(self):
		x = self.filepath
		y = self.file_in
		return x, y

	def total_word(self):
		with open(self.file_in, "r") as myfile:
			myfiles = myfile.read()
			counting = len(myfiles.split())
			myfile.close()
			print("\nThe total words in your file:", counting)

	def count_words(self):
		with open(self.file_in, "r") as myfile:
			myfiles = myfile.read()
			for punct in string.punctuation: #developed by S. Shakya
				myfiles = myfiles.replace(punct, "")
			myfiles = myfiles.replace("\n\n", "").replace("\n", "").strip()
			list1 = re.split(' ', myfiles)
			numbers = Counter(list1).most_common(20)
			myfile.close()
		return numbers

	def type_punct(self):
		with open(self.file_in, "r") as myfile:
			myfiles = myfile.read()
			list2 = string.punctuation
			my_dict = {}
			for punct in list2:
				a = myfiles.count(punct)
				if a > 0:
					my_dict[punct] = a
			myfile.close()
		return my_dict

	def print_type_punct(self):
		print("\nTypes of punctuation in file:")
		for punct in self.type_punct().keys():
			print(punct)
		
	def count_punct(self):
		return sorted(self.type_punct().items(), key=lambda item: -item[1])[0:10]
	
	
def main():
	args = user_input()
	a = Countme(args.file_in)
	aa = a.file_info()
	print("\nThis is your file path and file name:\n", aa)
	counts = a.count_words()
	print("\nYour total counts of words from input file is: \n")
	for item in counts:
		print("{} {}".format(item[1], item[0]))
	punct = a.count_punct()
	print("\nYour total counts of punctuation from input file is: \n")
	for item in punct:
		print("{} {}".format(item[1], item[0]))


if __name__ == '__main__':
    main()
