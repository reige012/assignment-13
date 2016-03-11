#!/usr/bin/env python
# utf-8

"""
Task 1 of assignment 13
Created by Pramod Pantha on 9 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""

import random


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
# inside class Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)

                self.cards.append(card)
# inside class Deck:

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

# inside class Deck:
    def pop_card(self):
        return self.cards.pop()

# inside class Deck:
    def add_card(self, card):
        return self.cards.append(card)

# inside class Deck:
    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()


class Hand(Deck):
    """Represents a hand of playing cards."""

# inside class Hand:
    def __init__(self, label=''):
        self.cards = []
        self.label = label

# inside class Deck:
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

    queen_of_clubs = Card(1, 12)
    king_of_diamonds = Card(2, 13)
    print(queen_of_clubs)
    print(king_of_diamonds)

    get_rank = Card.rank_names[queen_of_clubs.rank]
    print(get_rank)

    hand = Hand('new hand')
    print(hand.label)

    deck = Deck()
    card = deck.pop_card()
    hand.add_card(card)
    print(hand)

if __name__ == '__main__':
    main()
