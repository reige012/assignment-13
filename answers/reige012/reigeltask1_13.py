#!/usr/bin/env python
# encoding: utf-8

"""
This program creates three new classes: Card(), Deck() and Hand() and then adds
specific methods and attributes to them. This is based on the python book found
on www.greenteapress/thinkpython2/html/thinkpython2019.html website (Ch18 Example).
It also prints pieces of the code results to show that its working properly.


Edited by Alicia Reigel. 9 March 2016.
Copyright Alicia Reigel. Louisiana State University. 9 March 2016. All
rights reserved.

"""


import random


class Card():
    """A class that represents a standard playing card.
    To create an instance of Card() you will list its Suit and Rank as integers
    (Suits can have integer values of 0-3 and Ranks of (None=0, 13=King))
    For example Queen_of_Hearts = Card(2, 12)"""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    # these are both class attributes of Card()

    def __init__(self, suit=0, rank=2):
        """defines the instance attributes of the Card() class"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """returns the Card() in a nice format for printing"""
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        """this function compares cards with suits being most important"""
        # checks the suits then the ranks and returns the higher card
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck():
    """ This function creates a whole set (Deck()) of cards, building on the Card() class already defined"""
    def __init__(self):
        """creates the whole deck of cards and adds them to a list"""
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns the cards in the deck in readable format"""
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        """Pulls a card from the bottom of the deck."""
        return self.cards.pop()

    def add_card(self, card):
        """Allows you to add a card to the deck."""
        self.cards.append(card)

    def shuffle(self):
        """shuffles the deck of cards. modifies the original deck."""
        random.shuffle(self.cards)

    def sort(self):
        """sorts the cards based on the ___lt__ method defined in cards"""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Deals a hand of the desired number of cards"""
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """This class makes a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, meth_name):
    """finds the class that a method belongs to"""
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


def main():
    deck = Deck()
    print("This is my deck:")
    print(deck)
    deck.shuffle()
    print("This is my deck after its been shuffled:")
    print(deck)
    deck.sort()
    print("This is my deck after being sorted:")
    print(deck)
    hand = Hand()
    card = deck.pop_card()
    hand.add_card(card)
    print("This is my hand after 1 instance of method pop_card:")
    print(hand)
    card2 = deck.pop_card()
    hand.add_card(card2)
    print("This is my hand after 2 pop_cards:")
    print(hand)
    new_hand = Hand()
    deck.move_cards(new_hand, 4)
    print("this is my new hand:")
    print(new_hand)
    whatisit = find_defining_class(hand, 'add_card')
    print("This is the class of object hand method add_card:")
    print(whatisit)


if __name__ == '__main__':
    main()
