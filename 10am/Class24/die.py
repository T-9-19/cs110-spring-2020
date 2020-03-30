"""
File: die.py
Author: Darren Strash
This module has a Die class that can be used to represent a 6-sided die.
"""

import random

class Die:

    def __init__(self):
        self.value = 0

    def roll(self):
        #self indicates the current object or instance of Die class
        #every method has self as an argument
        self.value = random.randint(1,6)

    def get_value(self):
        return self.value

def main():
    d1 = Die()
    d1.roll() # roll changes attribute for object d1
    v1 = d1.get_value()

    d2 = Die()
    d2.roll()
    v2 = d2.get_value()

    num_rolls = 1
    while v1 != v2:
        d1.roll() # roll changes attribute for object d1
        d2.roll()
        num_rolls += 1
        v1 = d1.get_value()
        v2 = d2.get_value()
    print("Number of rolls", num_rolls)

if __name__ == "__main__":
    main()
