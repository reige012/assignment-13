#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 13.

 Created by A.J. Turner on March 8, 2016. Helpful instructions/hints provided by S. Shakya. Original example for creating a class "Card" from:http://www.greenteapress.com/thinkpython2/html/thinkpython2019.html
 Copyright 2016 A.J. Turner. All rights reserved.

"""

import random

class Card:
	""" Represents a playing card. """
	
	def __init__(self, suit=0, rank=2):
		#setting up encoding of suits and ranks of cards - instance attributes
		self.suit = suit
		self.rank = rank
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	
	def __str__(self):
		""" Assigning class attributes of object Card """
		return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
	
	
	def __lt__(self, other):
		""" Comparing card values using lt (less than) special method"""
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return t1 < t2

class Deck:
	""" creating a deck of cards by making Deck a class"""
	
	def __init__(self):
		self.cards = []
		for suit in range(4): #enumerates suits 0 to 3 (4 suits)
			for rank in range(1,14): #enumerates ranks of cards from 1 to 13 and creates new card each loop
				card = Card(suit, rank)
				self.cards.append(card) #putting cards into the deck
	
	
	def __str__(self):
		""" string method called to create a string of cards and their associated suit/rank """
		res = [] #placeholder for the string
		for card in self.cards: #for card in deck (aka self.cards)
			res.append(str(card)) #building a list strings (cards)
		return '\n'.join(res) #joining the list of strings to make one large string
		# cards joined into one string; each card separated by a new line


	def pop_card(self):
		return self.cards.pop() #takes out last card in list (bottom of deck)
		
	
	def add_card(self):
		return self.cards.append(card) #adds card to deck
	
	
	def shuffle(self):
		random.shuffle(self.cards) #shuffles the deck
	
	
	def sort(self):
		self.cards.sort()
	
	
	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop.card())
	
class Hand(Deck):
	""" using inheritance to modify class Deck """
	def __init__(self, label=''):
		self.cards = [] #placeholder
		self.label = label
		
	
	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())
		
		
def main():
	card1 = Card(2,11) #creates a card
	print("\n The card made is: \n", card1)
	deck = Deck()
	print("\n Deck of cards: \n\n", deck)
	deck.shuffle() #shullfe deck
	print("\nShuffle deck example:\n\n", deck)
	hand = Hand('new hand') #creating a hand of cards (new long string, depending on value for num)
	deck.sort()
	print("\n The deck has been sorted\n\n", deck) #prints deck of cards (one long string)


if __name__ == '__main__':
	main()