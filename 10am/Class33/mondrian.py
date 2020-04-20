"""
    mondrian.py
    Darren Strash
    An interactive art piece inspired by Piet Mondrian.
"""

from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

COLORS = ["red", "blue", "yellow", "white", "black"]

class Mondrian(EventHandler):
    """ Makes interactive paintings like Piet Mondrian. """

    # The direction to split the Mondrian rectangle.
    # This needs to be a class variable so that all Mondrian objects have the
    # same value.
    split_direction = "v"

    def __init__(self, win, x_left, x_right, y_top, y_bottom, depth):
        """ Initialize a "splittable" rectangle for an interactive Mondrian
            painting. """
        EventHandler.__init__(self)
        self._win = win
        self._x_left = x_left
        self._x_right = x_right
        self._y_top = y_top
        self._y_bottom = y_bottom
        self._depth = depth

        center = ((x_left + x_right) // 2, (y_top + y_bottom) // 2)
        width = x_right - x_left
        height = y_bottom - y_top

        self._rect = Rectangle(win, width, height, center)
        self._win.add(self._rect)
        self._rect.add_handler(self)
        self._rect.set_fill_color(random.choice(COLORS))
        self._rect.set_depth(depth)

    def handle_mouse_press(self, event):
        """ Split the Mondrian Rectangle into two new Mondrian rectangles based
            either in the vertical or horizontal direction. """

        #This gets the location where the mouse was clicked
        (x_split, y_split) = event.get_mouse_location()
        if Mondrian.split_direction == "v":
            #split rectangle vertically
            Mondrian(self._win, self._x_left, x_split, self._y_top, self._y_bottom, self._depth - 1)
            Mondrian(self._win, x_split, self._x_right, self._y_top, self._y_bottom, self._depth - 1)
        elif Mondrian.split_direction == "h":
            #split rectangle horizontally
            Mondrian(self._win, self._x_left, self._x_right, self._y_top, y_split, self._depth - 1)
            Mondrian(self._win, self._x_left, self._x_right, y_split, self._y_bottom, self._depth - 1)

    def handle_key_press(self, event):
        """ Stores whether h or v key was pressed most recently on keyboard. """
        key = event.get_key()
        #ignore all keys except for "v" and "h"
        if key == "v":
            Mondrian.split_direction = "v"
        elif key == "h":
            Mondrian.split_direction = "h"


def main(win):
    """ The main function. """
    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    Mondrian(win, 10, WIN_WIDTH - 10, 10, WIN_HEIGHT - 10, 100)

if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
