# !/usr/bin/env python
# encoding: utf-8

"""
Program that contains examples from textbook chapter 18

Created by Andre Moncrieff on 9 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

"""

import random


class Card:
    """Represents a standard playing card."""
    def __init__(self,
                 suit=0,
                 rank=2,
                 ):
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["None", "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

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
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle(self):
        return random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()


class Hand(Deck):
    def __init__(self, label=" "):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


def main():
    card1 = Card(0, 2)
    #print(card1)
    deck = Deck()
    # print(deck)
    # deck.add_card("King of Chimes")
    # print(deck)
    # deck.pop_card()
    # deck.pop_card()
    # print(deck)
    # deck.shuffle()
    # print(deck)
    # deck.sort()
    # hand = Hand('lucky')
    # card = deck.pop_card()
    # card1 = deck.pop_card()
    # hand.add_card(card)
    # hand.add_card(card1)
    # hand.move_cards(hand,1)
    # print(hand)
    #print(deck)


if __name__ == '__main__':
    main()
