#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2016
- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program includes the requested attributes and methods (4.0 pt)
- [ ] Program demonstrates it's functionality (e.g. show it working from `main()` or similar) (2.0 pt)

@author: York
'''

import random
from numpy import rank


class Card:
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    suit_names=['CLubs','Diamonds','Hearts','Spades']
    rank_names=[None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    
    def __it__(self,other):
        if self.suit<other.suit:return True
        if self.suit>other.suit:return False
        return self.rank<other.rank
    
    
    def add_card(self,card):
        self.cards.append(card)
        return


class Deck:
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(suit,rank)
                self.cards.append(card)
    
    
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    
    def pop_card(self,i=1):
        return self.cards.pop()
    
    
    def add_card(self,card):
        self.cards.append(card)
        return
        
        
    def shuffle(self):
        random.shuffle(self.cards)
        return
        
    
    def sort_card(self,card):
        self.cards.sort
        self.cards = [] 
        for rank in range(1,14):
            for suit in range(4):
                self.cards.append(Card(suit, rank))
        #return self.cards
        
        
    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())
        return


class Hand(Deck):
    def __init__(self,label=''):
        self.cards=[]
        self.label = label
        
       
def main():
    queen_of_diamonds = Card(1,12)
    #print(queen_of_diamonds)
    card1 = Card(2, 9)
    #print(card1)
    result = Card.__lt__(queen_of_diamonds, card1)
    #print(result)
    deck = Deck()
    print(deck)
    deck.add_card(queen_of_diamonds)
    print(deck)
    deck.pop_card(queen_of_diamonds)
    print(deck)
    shuffled_deck = deck.shuffle()
    print(shuffled_deck)
    deck.sort_card(queen_of_diamonds)
    print(deck)
    hand=Hand('new hand')
    hand.cards
    print(deck)
    deck=Deck()
    card=deck.pop_card()
    hand.add_card(card)
    print(hand)
    deck.move_cards(hand, 5)
    print(deck)
       
if __name__ == '__main__':
    main()