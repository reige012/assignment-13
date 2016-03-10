#! /usr/bin/env python
# encoding UTF-8

'''
Assignment13Task1 biol7800
ZacCarver 03/10/2016
'''

from __future__ import print_function, division
import random


class Card:

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10'
                  'Jack', 'Queen', 'King']

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank],
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


class Hand(Deck):
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
    deck = Deck()
    print(deck)
    jack_of_spades = Card(3, 11)
    print(jack_of_spades)
    hand = Hand()
    deck.move_cards(hand, 2)
    hand.sort()
    print(hand)

if __name__ == '__main__':
    main()
