"""
File: warmup.py
Author: Darren Strash
Implement a print_suit_summary method for the Deck class.
"""
import random

RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
SUITS = ["D", "C", "S", "H"]

FACE_CARD_VALUE = 10
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11
HIGHEST_HAND_VALUE = 21

class PlayingCard:
    """ A playing card for the game black jack. """

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
    """ A deck of playing cards for the game blackjack. """

    def __init__(self):
        """ Construct a shuffled standard 52-card deck of playing cards. """
        self._deck_list = []
        for rank in RANKS:
            for suit in SUITS:
                playing_card = PlayingCard(rank, suit)
                self._deck_list.append(playing_card)
        self.shuffle()

    def __repr__(self):
        """ Return a string representation of the deck of playing cards. """
        return str(self._deck_list)

    def shuffle(self):
        """ Shuffle the deck of playing cards. """
        random.shuffle(self._deck_list)

    def draw_one_card(self):
        """ Remove and return one playing card from the deck. """
        return self._deck_list.pop()

    def print_suit_summary(self):

        num_hearts = 0
        num_clubs = 0
        num_spades = 0
        num_diamonds = 0

        for card in self._deck_list:
            if card.get_suit() == "H":
                num_hearts += 1
            elif card.get_suit() == "C":
                num_clubs += 1
            elif card.get_suit() == "S":
                num_spades += 1
            else:
                num_diamonds += 1

        print("Number of hearts={}".format(num_hearts))
        print("Number of clubs={}".format(num_clubs))
        print("Number of spades={}".format(num_spades))
        print("Number of diamonds={}".format(num_diamonds))


class Hand:
    """ A class for storing a hand of playing cards in blackjack. """

    def __init__(self):
        """ Construct an empty hand with an empty list. """
        self._hand_list = []

    def __repr__(self):
        """ Returning a string representation of the hand. """
        return str(self._hand_list)

    def take_into_hand(self, playing_card):
        """ Including a new playing card into our hand. """
        self._hand_list.append(playing_card)

    def value(self):
        """ Compute the value of the hand as would do in blackjack
            i.e., if having an ace's value be 11 would push total
            value over 21, treat it as a 1. """
        sum_hand = 0
        num_aces = 0
        for card in self._hand_list:
            if card.is_face():
                sum_hand += FACE_CARD_VALUE
            elif card.get_rank() == "A":
                sum_hand += ACE_LOW_VALUE
                num_aces += 1
            else:
                sum_hand += card.get_rank()

        for ace in range(num_aces):
            if sum_hand + ACE_HIGH_VALUE - ACE_LOW_VALUE <= 21:
                sum_hand += ACE_HIGH_VALUE - ACE_LOW_VALUE
        return sum_hand


def main():
    """ Make a deck of playing cards and draw two cards."""
    deck = Deck()
    deck.print_suit_summary()
    hand = Hand()
    # # print("Our starting hand: {} ".format(hand))
    hand.take_into_hand(deck.draw_one_card())
    hand.take_into_hand(deck.draw_one_card())
    hand.take_into_hand(deck.draw_one_card())
    print("Our hand after drawing: {} has value {} ".format(hand, hand.value()))
    deck.print_suit_summary()



if __name__ == "__main__":
    main()
