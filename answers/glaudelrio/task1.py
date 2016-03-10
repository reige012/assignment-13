#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:24:22 2016

@author: Glaucia
"""
"""
Task1
"""
import random


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
   
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    #creating the method sort
    def sort(self):
        return self.cards.sort()


class Hand(Deck):

     def __init__(self, label=''):
        self.cards = []
        self.label = label
    
     def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())



def main():
    card1 = Card(3, 9)
    print(card1)
    deck = Deck()
    print(deck)
    deck.sort()
    print(deck)
    deck.add_card("Joker")
    print(deck)
    hand = Hand('new hand')
    hand.cards
    hand.label
    card = deck.pop_card()
    hand.add_card(card)
    print(hand)

    
    
if __name__ == '__main__':
    main()      


