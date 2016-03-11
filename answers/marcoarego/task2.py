# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:09:07 2016

@author: Marco
"""

import collections
import re
import argparse
import string
import operator
import os



def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description="""my argument parser""")
    # Adding an argument to 'parse'        
    parser.add_argument('in_file', type=str, 
                        help='after placing your file and script in the same '
                        'folder, type the name of your file after the name '
                        'of this script in the terminal.')
    args = parser.parse_args()
    inp = args.in_file
    return inp


class WordCounting:
    '''
    this class will work on text files to count word occurrences
    '''        

    def __init__(self,filename):
        self.filename = filename
        self.filepath = os.path.abspath("self.filename")
    
    def file_opener(self,filename):
        '''
        Opens and transform a txt file in to a string
        '''
        my_list = []   
        with open(self.filename,'r') as darwin:
            for line in darwin:
                item = re.sub("\s+"," ",line)
                my_list.append(item.strip())
        for my_string in my_list:
            if len(my_string) == 0:
                my_list.pop(my_list.index(my_string))
        my_fused_string = ' '.join(my_list)
        return my_fused_string
        
    def string_standizer(self):
        '''
        this function takes all kinds of pontuation out of our string, including
        the apostrophe (') of words like can't, for example. The output will
        comprehend a lower case string with words separated by spaces.
        '''
        low = self.file_opener(self.filename).casefold()
        new_lines_out = re.sub("\n"," ",low)
        without_apos = re.sub("'","",new_lines_out)
        without_pontuation = re.sub("\W"," ",without_apos)
        one_space = re.sub("\s+"," ",without_pontuation)
        end_stripper = one_space.strip()
        return end_stripper

    def total_word_count(self):
        '''
        Counts total number of words in a txt document
        '''
        standard_text = self.string_standizer()
        wordlist = standard_text.split(" ")
        return len(wordlist), wordlist
        
    def counter_function(self,n):
        '''
        The input is a string. 
        this function uses the Counter function from the collections' module to
        count the values in a list and return a dictionary with the number of
        occurrencies for each word
        '''
        string_list = self.string_standizer()
        listagem = string_list.split(" ")
        count = collections.Counter(listagem)
        more_freq = count.most_common(n)
        return more_freq           
    
    def get_words_by_letter(self, letter='a'):
        '''
        Retrieve a list of words, and their counts, that starts with any desired 
        letter. The output resembles the one from the function list_packer.
        '''    
        desired_words=[]
        for word in self.total_word_count()[1]:
            if word[0]==letter:
                word = re.sub("\W","",word)
                word = word.lower()
                desired_words.append(word)
            else:
                pass
        return desired_words

    def punctuation_counter(self):
        '''
        This method counts the punctuation in a text
        '''
        text=self.file_opener(self.filename)
        counts = collections.Counter(text)
        punctuation_counts = {k:v for k, v in counts.items() if k in string.punctuation}
        sorteddict=dict(sorted(punctuation_counts.items(), 
                               key=operator.itemgetter(1), reverse=True)[:10])
        dictlist=[] 
        for key, value in sorteddict.items():
            newlist = [value,key]
            dictlist.append(newlist)
        listofpoints=(sorted(dictlist, reverse=True))
        return listofpoints

    def punctuation_types(self):
        points=self.punctuation_counter()
        types=[]
        for point in points:
            types.append(point[1])
        return(types)

    def super_displayer(self):
        print("\nTop 20 words:")
        for word, count in self.counter_function(20):
            print(' {:4} ---> {:>3}'.format(word,count))
        print("\nTop ten punctuations:")
        for p_count, punct in self.punctuation_counter():
            print(' {:2} ---> {:>3}'.format(punct,p_count))
        #pass


def main():
    inp = parser_function()
    result = WordCounting(inp)
    result.punctuation_counter()
    result.total_word_count()[0]
    result.counter_function(20)
    result.super_displayer()


if __name__ == '__main__':
    main()
