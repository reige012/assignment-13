#!/usr/bin/env python
# encoding: utf-8

"""This is code for chapter 18 or assignment 13.

Copyright 2015 Allen Downey

"""

from __future__ import print_function, division

import random


class Card:
    """Represents a standard playing card.

    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.

        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        return self.cards.append(card)

    def remove_card(self, card):
        return self.cards.remove(card)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


    def move_cards(self, hand, num):
        for i in range(num):
            return hand.add_card(self.pop_card(-1))


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


def main():
        deck = Deck()
        print(deck)

        hand = Hand('new hand')
        hand.cards
        []
        print(hand.label)

        deck = Deck()
        card = deck.pop_card()
        hand.add_card(card)
        print(hand)


if __name__ == '__main__':
    main()
