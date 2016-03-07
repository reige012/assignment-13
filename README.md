# Task 1

Work your way through the entire card/deck example of **inheritance** that is given in [Chapter 18](http://www.greenteapress.com/thinkpython2/html/thinkpython2019.html) of our book. By the time you finish, you should have created a file containing three classes (`Deck()` and `Card()` and `Hand()`).  Be sure to include all the attributes/methods covered in the example.  Also be sure to include the `Deck.sort()` method that is requested.  You can use a `main` function to demonstrate (and show yourself) how these classes work independently and together.


# Task 2

Rethink your word-counting code just a little bit.  How could you parse and summarize words in a text file using an object-oriented approach?  Write a class that operates generically, on any file, to summarize word counts.  Specifically, write a class that includes or computes the following attributes:

* file name (this is the name of the actual file)
* file path (this is the path to the file)
* total number of words in file
* type of puncutation used in the file

And also that includes the following methods (these may not be all you need, just the ones you must have):

* a method to count words
* a method to count punctuation
* a method to display both of these results

Your program should contain a main loop and an ifmain statement, it should be formatted correctly, and you should use argparse to get the name of the input file from the user.  Your program should display, to the user, (1) the top 20 words and their counts, and (2) the top 10 puncation marks and their counts.  You do not need to write any results to an outfile.  Be sure to include the file(s) that you used to test/design your program.
