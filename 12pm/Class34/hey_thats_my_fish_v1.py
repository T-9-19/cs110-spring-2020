"""
    hey_thats_my_fish_v1.py
    Darren Strash and CS 110
    Implementation of Hey That's My Fish.
"""

from cs110graphics import *
import random, math

WIN_WIDTH = 800
WIN_HEIGHT = 800

TILE_DIAMETER = WIN_WIDTH // 8
TILE_RADIUS = TILE_DIAMETER // 2
TILE_FONT_SIZE = 20

NUM_ROWS = 8

PENGUIN_RADIUS = 15

class Tile(EventHandler):
    """ A class to represent a tile in the game Hey That's My Fish! """

    def __init__(self, win, row, col):
        """ Construct the tile, placing it into correct position based on its
            row and column, and give it a random number of fish. """

        EventHandler.__init__(self)
        self._win = win
        self._row = row
        self._col = col
        self.center_from_row_col()
        self._circle = Circle(win, TILE_RADIUS, self._center)
        self._circle.set_depth(100)
        self._win.add(self._circle)
        self._fish = random.randint(1,3)
        self._text = Text(win, str(self._fish), TILE_FONT_SIZE, self._center)
        self._text.set_depth(50)
        self._win.add(self._text)

        self._circle.add_handler(self)
        self._text.add_handler(self)

    def center_from_row_col(self):
        """ Get the center from a particular row and column. """

        center_x = TILE_RADIUS + TILE_DIAMETER * self._col
        if self._row % 2 == 1:
            center_x += TILE_RADIUS

        center_y = TILE_RADIUS + int((TILE_RADIUS * math.sqrt(3)) * self._row)

        self._center = (center_x, center_y)

    def add_penguin(self, color):
        """ Add a penguin to the tile. """

        self._penguin = Circle(self._win, PENGUIN_RADIUS, self._center)
        self._penguin.set_depth(25)
        self._penguin.set_fill_color(color)
        self._win.add(self._penguin)

    def handle_mouse_press(self, event):
        """ Add a green penguin when clicking the tile. """

        self.add_penguin("green")


class HeyThatsMyFish:
    """ A class to control the overall game of Hey That's My Fish! """


    def __init__(self, win):
        """ Construct the class with the game components (currently tiles). """

        self._win = win
        self._win.set_background("lightblue")

        self._tiles = []
        for row in range(NUM_ROWS):
            self._row_list = []
            num_cols = 8
            if row % 2 == 1:
                num_cols = 7

            for col in range(num_cols):
                self._row_list.append(Tile(win, row, col))


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    hey = HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """

    StartGraphicsSystem(main)
