#!/usr/bin/env python

"""
Assignment_13: Task1
Working through exercise in Chapter 18

Worked on the example on: March 9, 2016

"""

import random


class Card:
    """Represents a standard playing card."""
    suit_names = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                'Jack', 'Queen', 'King']


    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        # Returns a human-readable string representation.
        return '{} of {}'.format(Card.rank_names[self.rank],
                                 Card.suit_names[self.suit])


    def __lt__(self, other):
        # compares this card to other, first by suit and then by rank
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """below is class definition for Deck. The init method created the \
    attribute cards and generates standard set of 52 cards."""
    def __init__(self):
        self.cards = []
        # the following is an example of nested loop
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)


    def __str__(self):
        # Returns a string representation of the deck.
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
        # join is a string method


    def pop_card(self):
        # Removes last card from the deck and returns to it.
        return self.cards.pop


    def add_card(self, card):
        self.cards.append(card)


    def shuffle(self):
        # Shuffles the cards in this deck.
        random.shuffle(self.cards)


    def sort(self):
        # Sorts the cards in ascending order.
        self.cards.sort()


    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop(card))


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def main():
    queen_of_cards = Card(1, 12)
    card1 = Card(2, 11)
    print(card1)
    deck = Deck()
    print(deck)
    hand = Hand('new hand')
    hand.label
    card = deck.pop_card()
    hand.add_card(card)
    print(hand)


if __name__ == '__main__':
    main()
