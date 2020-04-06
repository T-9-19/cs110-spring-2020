"""
File: blackjack2.py
Author: Darren Strash
Implement classes for a blackjack game.
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

class Player:
    """ A class to support a single player playing blackjack. """

    def __init__(self, name, deck):
        """ Instantiate the class with an empty hand, a given name and deck. """
        self._name = name
        self._hand = Hand()
        self._deck = deck

    def get_name(self):
        """ Return the players name. """
        return self._name

    def value(self):
        """ Return the value of the player's hand. """
        return self._hand.value()

    def draw_card(self):
        """ Draw a card into the player's hand. """
        self._hand.take_into_hand(self._deck.draw_one_card())

    def get_hand(self):
        """ Return the player's hand. """
        return self._hand

    def hit_or_stay(self):
        """ Interactively decide whether the player should hit or stay. Force
            player to stay if hand value is over 21. """
        print("{} has hand {} with value {}"
                    .format(self._name, self._hand, self.value()))
        if self.value() > 21:
            return True #stay

        option = input("Do you want to hit (h) or stay (s)? ")

        if option == "h":
            self.draw_card()
            return False #hit
        else:
            return True #stay

def main():
    """ Make a deck of playing cards and draw two cards."""
    deck = Deck()

    eleanor = Player("Eleanor", deck)
    chidi   = Player("Chidi", deck)
    michael = Player("Michael", deck)

    players = [eleanor, chidi, michael]

    for player in players:
        player.draw_card()
        player.draw_card()
        print("Player {} has hand {}".format(player.get_name(), player.get_hand()))

    for player in players:
        stay = False
        while not stay:
            stay = player.hit_or_stay()

    player_with_highest_score = None
    highest_score = 0
    for player in players:
        if player.value() <= 21 and player.value() > highest_score:
            highest_score = player.value()
            player_with_highest_score = player

    print("{} wins with a score of {}!"
        .format(player_with_highest_score.get_name(),
                highest_score))

    # hit or stay, use value when deciding, end by staying
    # above 21, you lose (bust)



if __name__ == "__main__":
    main()
