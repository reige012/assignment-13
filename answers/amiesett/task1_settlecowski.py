#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 13 Task 1

Amie Settlecowski
10 Mar. 2016

This file contains defines 3 classes: Deck(), Card(), and Hand()
From Think Python 2, Chapter 18,
"""


import random


class Card():
    '''Represents a standard playing card.'''
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8',
                    '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '{0} of {1}'.format(Card.rank_names[self.rank],
                                    Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return t1 < t2


class Deck():
    '''Represents standard deck of 52 playing cards.'''
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
        '''Remove and return value of last Card object from Deck object'''
        return self.cards.pop()

    def add_card(self, card):
        '''Add Card object to end of list that makes up Deck object'''
        self.cards.append(card)

    def shuffle(self):
        ''''Randomize' order of Card objects in Deck object'''
        random.shuffle(self.cards)

    def move_cards(self, other_card_group, num):
        '''
        Move specified number of cards from self to another Deck/Hand object
        '''
        for i in range(num):
            other_card_group.add_card(self.pop_card())

    def sort_cards(self):
        '''Sort cards by suit and then rank in descending order'''
        self.cards.sort()


class Hand(Deck):
    '''Represents a hand of playing cards.'''
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def main():
    # test Card class
    print('Testing Card class: ''\n''Printing 2 Card objects:')
    card = Card(1, 12)
    card1 = Card(2, 11)
    print(card, card1)
    # test Deck class
    print('\n''Testing Deck class:''\n''Printing a Deck object:')
    deck = Deck()
    print(deck)
    # print('\n''Testing shuffle method:''\n''Printing part of a shuffled Deck object:')
    deck.shuffle()
    # print(deck)
    # print('\n''Testing sort_cards method:''\n''Printing part of a sorted Deck object:')
    deck.sort_cards()
    # print(deck)

    # test Hand class
    print('\n''Testing Hand class:''\n''Printing an empty hand object:')
    hand = Hand('new hand')
    deck.shuffle() # cards printed in hand should not be ordered
    # deal one card to hand using combination of Deck methods
    print('\n''Printing a hand of 1 card:''\n')
    card = deck.pop_card()
    hand.add_card(card)
    print(hand)
    # deal 4 cards to hand using new move_cards method in Deck
    print('\n''Printing a hand of 5 cards:''\n')
    deck.move_cards(hand, 4)
    print(hand)
    print(len(deck.cards), " cards remaining in deck.")

if __name__ == '__main__':
    main()
