"""
File: blackjack.py
Author: Darren Strash
Implement classes for a blackjack game.
"""
import random

RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
SUITS = ["D", "C", "S", "H"]

class PlayingCard:

    def __init__(self, rank, suit):
        """ Constructs a playing card with given rank and suit. """
        self._rank = rank
        self._suit = suit

    def __str__(self):
        """ Returns the string representation of the playing card. """
        return str(self._rank) + self._suit

    def __repr__(self):
        """ Returns the string representation of the playing card. """
        return self.__str__()

    def get_rank(self):
        """ Return the rank of the playing card. """
        return self._rank

    def get_suit(self):
        """ Return the suit of the playing card. """
        return self._suit

    def is_face(self):
        """ Return True if and only if the playing card is a face card. """
        return self._rank == "J" or \
               self._rank == "Q" or \
               self._rank == "K"

class Deck:

    def __init__(self):
        """ Construct a shuffled standard 52-card deck of playing cards. """
        self._deck = []
        for rank in RANKS:
            for suit in SUITS:
                playing_card = PlayingCard(rank, suit)
                self._deck.append(playing_card)
        self.shuffle()

    def __repr__(self):
        """ Return a string representation of the deck of playing cards. """
        return str(self._deck)

    def shuffle(self):
        """ Shuffle the deck of playing cards. """
        random.shuffle(self._deck)

    def draw_one_card(self):
        """ Remove and return one playing card from the deck. """
        return self._deck.pop()

def main():
    """ Make a deck of playing cards and draw two cards."""
    deck = Deck()
    print(deck)
    print("Drew:", deck.draw_one_card())
    print("Drew:", deck.draw_one_card())
    print(deck)


if __name__ == "__main__":
    main()
