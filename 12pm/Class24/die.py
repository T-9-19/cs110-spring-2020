"""
File: die.py
Author: Darren Strash
This module has a Die class that can be used to represent a 6-sided die.
"""

import random

class Die:
    def __init__(self):
        """ Constructor for Die class, initialize different attributes """
        self.value = self.roll()

    def roll(self):
        """ Method to roll die and set value attribute."""
        self.value = random.randint(1,6)

    def get_value(self):
        """ Return the current value of the die."""
        return self.value

def main():
    d = Die()
    d.roll()

    d2 = Die()
    d2.roll()

    roll_num = 1
    while d.get_value() != d2.get_value():
        roll_num += 1
        d2.roll()
        d.roll()

    print("Number of rolls until same:", roll_num)

if __name__ == "__main__":
    main()
