#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
1 March 2016
Assignment 13 Task 1

Chapter 18 in Think Python
'''

import random


class Card:

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = [None, 'Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return "{} of {}".format(Card.rank_names[self.rank],
                                    Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
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


def main():
    my_card = Card(1, 12)
    print(my_card)
    deck1 = Deck()
    print("\n\nDECK 1:\n", deck1)
    deck2 = deck1.add_card(my_card)
    print("\n\nDECK 2:\n", deck2)
    a_card = Deck.pop_card()
    print(a_card)

if __name__ == '__main__':
    main()
