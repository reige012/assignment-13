#!/usr/bin/env python
# encoding: utf-8
"""
create a file containing three classes (Deck() and Card() and Hand() from
 chapter 18
"""
import random


class Card:
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
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

    def add_card(self, card):
        return self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


def main():
    queen_of_diamonds = Card(1, 12)
    print(queen_of_diamonds)
    card1 = Card(2, 11)
    print(card1)
    result = Card.__lt__(queen_of_diamonds, card1)
    print(result)
    deck = Deck()
    print(deck)
    # popcard = Deck.pop_card(card)
    # print(popcard)
    deck.add_card(queen_of_diamonds)
    print(deck)
    deck.remove_card(queen_of_diamonds)
    print(deck)
    result2 = deck.pop_card()
    print(deck)
    deck.shuffle()
    print(deck)
    hand = Hand('new hand')
    print(hand.cards)
    print(hand.label)
    hand.add_card(result2)
    print(hand)
    deck.move_cards(hand, 6)
    print(hand)
    deck.sort()
    print(deck)
    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))


if __name__ == '__main__':
    main()
