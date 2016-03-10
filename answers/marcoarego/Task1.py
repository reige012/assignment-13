# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 07:38:37 2016

@author: Marco
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
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False              


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
    card1 = Card(1, 5)
    print(card1)
    print("\n")
    deck = Deck()
    print(deck)
    print("\n")
    deck.sort()
    print(deck)
    print("\n")
    deck.add_card("Joker")
    print(deck)
    print("\n")
    hand = Hand('new hand')
    hand.cards
    hand.label
    card = deck.pop_card()
    hand.add_card(card)
    print(hand)

    
    
if __name__ == '__main__':
    main()      