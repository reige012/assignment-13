#! usr/bin/env python
# encoding: utf-8

"""
Assignment 13
Task 1 Program: Inheritance Example from Think Python Chapter 18
Jessie Salter
8 March 2016
"""


class Card:
    '''Represents a standard playing card.'''
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

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


class Deck:
    '''Represents a standard deck of 52 playing cards.'''
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
        import random
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        '''Deals a given number of cards to a given hand.'''
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    '''Represents a hand of playing cards.'''
    def __init__(self, label='your hand'):
        self.cards = []
        self.label = label

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '{}:\n{}'.format(self.label, '\n'.join(res))


def main():
    deck = Deck()
    deck.shuffle()
    your_hand = Hand()
    deck.move_cards(your_hand, 5)
    my_hand = Hand('my hand')
    deck.move_cards(my_hand, 5)
    print('{}\n---\n{}'.format(your_hand, my_hand))


if __name__ == '__main__':
    main()
