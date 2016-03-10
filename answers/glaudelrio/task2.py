#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:17:21 2016

@author: Glaucia
"""
"""
Task2
"""

import collections
import re
import argparse
import string
import operator
import os



def arguments():
        """parsing arguments to allow changing input file and output name"""
        parser = argparse.ArgumentParser(description="""my argument parser""")   
        parser.add_argument('input', type=str, help='give the name of your input file')
        args = parser.parse_args()
        return args


class Counting_Words:
    """a class that allows counting the punctuation and ammount of words in a text"""
    
    def __init__(self,filename):
         self.filename = filename
         self.filepath=os.path.abspath("self.filename")
         self.totalwords = str(len(self.amountofwords()))
         self.typepunctuation=str(self.typeofpunctuation())
         
    def openningfile(self,filename):
        """opens a text file whose name is given as input in the shell. Returns a string that will be used
        in word counts"""
        storingfile=[]
        with open(self.filename,'r') as my_file:
            for line in my_file:
                storingfile.append(line)  
            self.text ="".join(storingfile)
        return self.text
    
    def countingpunctuation(self):
        """a method to count the punctuation in a text"""
        text=self.openningfile(self.filename)
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
    
    def typeofpunctuation(self):
        points=self.countingpunctuation()
        types=[]
        for point in points:
            types.append(point[1])
        return(types)
        
    def dealingtext (self):
        """edits a string removing ponctuation, spaces new lines, and capital letters
        to allow adequate word count. Returns the edited string"""
        text=self.openningfile(self.filename)
        text=re.sub("'","",text)
        text=re.sub('"',"",text)
        text=re.sub("\n","",text)
        text=re.sub("\W"," ",text)
        text=re.sub("\s+"," ",text)
        text=re.sub("-"," ",text)
        text=text.lower()
        finaltext=text.strip()
        return finaltext
    
    def amountofwords(self):
        """counts the words in the string provided in the last two functions, writes a file 
        with all the word counts (tab delimited). The argument filename takes the name of the file
        that will be writen. Returns a dictionary with all the words counts"""
        finaltext=self.dealingtext()
        wordlist = finaltext.split(" ")
        return wordlist
        
    def dictwords(self):
        wordlist=self.amountofwords()
        counterdict=collections.Counter(wordlist)
        return counterdict
   
    def countingtop20words(self):
        counterdict=self.dictwords()
        top20=counterdict.most_common(20)
        listoflists=(sorted(top20, key=lambda top20: top20[1],reverse=True))
        return listoflists
     
    def printtoppoints(self):
        """a method to print the top 10 punctuation"""
        listofpoints=self.countingpunctuation()
        print("my top 10 punctuation:")        
        for lis in listofpoints:
            line_new = "{0:<20} {1:1d}".format(lis[1],lis[0])
            print(line_new)     
    
    def printtop20(self):
        """a method to print the top 20 puntuation"""
        listoflists=self.countingtop20words()
        print("my top 20 words:") 
        for lis in listoflists:
            line_new = "{0:<20} {1:1d}".format(lis[0],lis[1])
            print(line_new) 
   
             
def main():
    arg=arguments()
    inpu=arg.input
    mytext=Counting_Words(inpu)
    mytext.printtop20()
    mytext.printtoppoints()
    print("one of the attributes of my class is the file name: " + mytext.filename)
    print("one of the attributes of my class is the file path: " + mytext.filepath)
    print("one of the attributes of my class is the total number of words: " + mytext.totalwords)
    print("one of the attributes of my class is a list with the types of punctuation: ", mytext.typepunctuation)
           
if __name__ == '__main__':
    main()      