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
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return str(self._rank) + self._suit

    def __repr__(self):
        return self.__str__()

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit

    def is_face(self):
        return self._rank == "J" or \
               self._rank == "Q" or \
               self._rank == "K"

class Deck:

    def __init__(self):
        self._deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = PlayingCard(rank, suit)
                self._deck.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._deck)

    def __str__(self):
        return str(self._deck)

    def deal_one_card(self):
        return self._deck.pop()

def main():

    deck = Deck()
    print("The original deck:", deck)
    print("Drawn card: ", deck.deal_one_card())
    print("Drawn card: ", deck.deal_one_card())

    print("The new deck:", deck)



    # real_card = PlayingCard("J", "D")
    # card_string = str(real_card)
    # print(card_string)
    # print(real_card)
    # print("Rank:", real_card.get_rank(), ", Suit:", real_card.get_suit())
    # print("Is Face?:", real_card.is_face())
    # print(real_card)


if __name__ == "__main__":
    main()
