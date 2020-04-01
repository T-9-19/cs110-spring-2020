"""
File: warmup.py
Author: Darren Strash
Add method repeated_roll to the Die class
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

    def repeated_roll(self, count):
        """ Return a list of count rolls of the die. """
        rolls = []
        for roll in range(count):
            self.roll()
            rolls.append(self.get_value())
        return rolls

def main():

    d = Die()
    rolls = d.repeated_roll(10)
    print(rolls)
    pass

if __name__ == "__main__":
    main()
