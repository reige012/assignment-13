# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 11
Oscar Johnson 4 March 2016
"""

import random


class Card:
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']


class Deck:
    """create a deck of cards"""
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
        return self.cards.append(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()


class Hand(Deck):
    """represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty



def main():
    deck1 = Deck()
    print(deck1)

    queen_of_diamonds = Card(1, 12)
    king_of_hearts = Card(2, 13)
    print(queen_of_diamonds)
    print(king_of_hearts)

    get_rank = Card.rank_names[queen_of_diamonds.rank] 
    print(get_rank)
    
    hand = Hand('new hand')
    print(hand.label)

if __name__ == '__main__':
    main()