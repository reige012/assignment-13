#!/usr/bin/env python
# utf-8

"""
Assignment 13, Task 1
Jon Nations on 9 March 2016
This creates 52 cards, puts them in a deck, shuffles them,
and sends them to a hand. Courtesy of
Think Python: How to Think Like a Computer Scientist
Chapter 18
http://www.greenteapress.com/thinkpython2/html/thinkpython2019.html

"""

import random


class Card:
    "Represents a standard playing card"

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    """called class attributes because they are associated with the class object Card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        """called instances (b/c you instantiate them) because they are associated with a particular instance. *** Every card has its own suit and rank, but there is only one copy of suit_names and rank_names."""

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        """This makes suit more important than rank"""
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        """The init method creates the attribute cards and generates the standard set of fifty-two cards. Each iteration creates a new Card with the current suit and rank, and appends it to self.cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Printing the Deck. This method demonstrates an efficient way to accumulate a large string: building a list of strings and then using the string method join. The built-in function str invokes the __str__ method on each card and returns the string representation."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
        # versus return '\n'.join(res)

    def pop_card(self):
        """The pop method removes a card from the deck and returns it"""
        return self.cards.pop()

    def add_card(self, card):
        """append adds a card to the deck"""
        return self.cards.append(card)

    def shuffle(self):
        """shuffles deck"""
        return random.shuffle(self.cards)

    def sort(self):
        """sorts deck after shuffle"""
        return self.cards.sort()

    def move_cards(self, hand, num):
        """moves x number of hards into a hand
        be sure to shuffle first! Otherwise the
        game is pretty dull."""
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    '''This represents a hand of playing cards'''

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def main():
    queen_of_diamonds = Card(1, 12)
    print("\nCARD 1, 12 IS THE", queen_of_diamonds)
    card1 = Card(2, 11)
    print("\nCARD 2,11 IS THE", card1)
    deck = Deck()
    print("\nTHIS IS THE WHOLE DECK \n\n", deck)
    deck.shuffle()
    print("\nTHIS DECK HAS BEEN SHUFFLED \n\n", deck)
    hand = Hand()
    deck.move_cards(hand, 5)
    hand.sort()
    print("\n THIS IS A NEW HAND\n\n", hand)
    deck.sort()
    print("\nTHIS DECK HAS BEEN SORTED \n\n", deck)


if __name__ == '__main__':
    main()
