#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2016
-[ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses `argparse` to get the input filename (1.0 pt)
- [ ] Program uses a class-based approach and includes the requested attributes and methods (4.0 pt)
- [ ] Program correctly counts and displays both words and puncutation in any file (2.0 pt)
@author: York
'''


import argparse
import os
import string
from collections import Counter


def path_file(filepath):
    filepath.add_argument("--input",required=True,type=str,help='Enter the file name')
    filepath.add_argument("--path",required=True,type=str,help='Enter the path of the file')
    

class FileCount():
    def __init__(self, file):
        self.file = input
        self.file_path = os.path.abspath(file)
        counts = self.gather(file)
        self.punct_counts = counts[1]
        self.word_counts = counts[0]
        self.punctuation = list(self.punct_counts.keys())
        self.word_count = len(self.word_counts.keys())
        
        
    def Clean(self, subst):
        subst1 = ''
        subst = subst.replace("\r\n", " ").lower()
        listofpunc = []
        for letter in subst:
            if letter in string.punctuation:
                listofpunc.append(letter)
            if letter.isalpha() or letter == ' ':
                subst1 += letter
        wordscollect = subst1.split(' ')
        return wordscollect, listofpunc
    
    
    def index(self, list, pointer):
        for item in list:
            pointer[item] += 1
        return pointer
    
    def gather(self, file):
        word_counter = Counter()
        punct_counter = Counter()
        with open(file, 'r') as file1:
            for line in file1:
                x = self.Clean(line)
                words = x[0]
                puncts = x[1]
                word_counter = self.index(words, word_counter)
                punct_counter = self.index(puncts, punct_counter)
            file1.close()
        return word_counter, punct_counter

 
    def __str__(self,):
        return '{}:\n{} words\n{} punctuation marks'.format(self.file_path,self.word_count,len(self.punctuation))


    def function1(self, pointer, rank):
        width = len(max(pointer, key=len))
        rank_counts = pointer.most_common(20)
        n = 0
        for index in rank_counts:
            if n < rank:
                print('{0:{3}{width}}{2}{1:{3}}'.format(index[0], index[1],'\t', '<', width=width))
            n += 1
        return n



def main():
    file_name_parser = argparse.ArgumentParser()
    path_file(file_name_parser)
    file_name_args = file_name_parser.parse_args()
    counts = FileCount(file_name_args.input)
    print('Twenty most common words:')
    counts.function1(counts.word_counts, 20)
    print('Ten most common punctuation marks:')
    counts.function1(counts.punct_counts, 10)

if __name__ == '__main__':
    main()
