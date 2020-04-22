"""
    hey_thats_my_fish_v1.py
    Darren Strash and CS 110
    Implementation of Hey That's my Fish.
"""

from cs110graphics import *
import random, math

WIN_WIDTH = 800
WIN_HEIGHT = 800

CIRCLE_DIAMETER = WIN_WIDTH // 8
CIRCLE_RADIUS = CIRCLE_DIAMETER // 2

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

        #get random number of fish
        self._fish = random.randint(1,3)
        self._has_penguin = False

        self._center = self.get_center_from_row_col()
        #using circles instead of hexagons (keep it simple)
        self._circle = Circle(self._win, CIRCLE_RADIUS, self._center)
        self._circle.set_depth(100)
        self._win.add(self._circle)

        self._text = Text(win, str(self._fish), 20, self._center)
        self._text.set_depth(50)
        self._win.add(self._text)

        self._circle.add_handler(self)
        self._text.add_handler(self)


    def get_center_from_row_col(self):
        """ Get the center from a particular row and column. """

        start_x = CIRCLE_RADIUS
        if self._row % 2 == 1:
            start_x = CIRCLE_DIAMETER
        real_x = start_x + CIRCLE_DIAMETER * self._col

        start_y = CIRCLE_RADIUS
        real_y = start_y + int(math.sqrt(3) * CIRCLE_RADIUS) * self._row
        return (real_x, real_y)

    def add_penguin(self, color):
        """ Add a penguin to the tile if it doesn't already have one. """

        if not self._has_penguin:
            self._penguin = Circle(self._win, PENGUIN_RADIUS, self._center)
            self._penguin.set_depth(25)
            self._penguin.set_fill_color(color)
            self._win.add(self._penguin)
            self._has_penguin = True

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
        for row in range(8):
            row_list = []
            even_row = row % 2 == 0

            num_cols = 7
            if even_row:
                num_cols = 8

            for col in range(num_cols):
                row_list.append(Tile(win, row, col))

            self._tiles.append(row_list)


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    hey = HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    
    StartGraphicsSystem(main)
