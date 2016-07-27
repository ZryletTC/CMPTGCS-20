#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from random import shuffle
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables represented as sets
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['♣','♢','♡','♠']

    def __init__(self,deck=[]):
        self.deck = deck # The deck is represented as a list and is initialy empty

        if (deck == []):
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    self.deck.append(Card(rank,suit))

    def __len__(self):
        return len(self.deck)

    def __repr__(self):
        return "Deck({})".format(self.deck)

    def __eq__(self,other):
        return self.deck == other.deck

    def dealCard(self):
        return self.deck.pop() # Remove and return a card from the end of the list

    def shuffle(self):
        shuffle(self.deck)
        
class Card:
    'represents a playing card'

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "Card('{}', '{}')".format(self.rank,self.suit)

    def __eq__(self,other):
        return (self.rank == other.rank and self.suit == other.suit)

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def printCard(self):
        print (self.rank +" "+ self.suit)
