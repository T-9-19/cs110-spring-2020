"""
    mondrian.py
    Darren Strash
    An interactive art piece inspired by Piet Mondrian.
"""

from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

COLORS = ["white", "black", "blue", "red", "yellow"]

class Mondrian(EventHandler):
    """ An interactive rectangle for Mondrian-inspired interactive artpiece. """
    #want as a class variable, so that all Mondrian objects will split in the
    #current split direction (have access to the same variable.)
    split_direction = "v"

    def __init__(self, win, x_left, x_right, y_top, y_bottom, depth):
        """ Initialize a Mondrian rectangle with a given location, depth and
            a random color. """
        EventHandler.__init__(self)
        self._win = win
        self._x_left = x_left
        self._x_right = x_right
        self._y_top = y_top
        self._y_bottom = y_bottom
        self._depth = depth

        center = ((x_left + x_right) // 2, (y_top + y_bottom) // 2)
        width  = x_right - x_left
        height = y_bottom - y_top

        rect = Rectangle(win, width, height, center)
        rect.add_handler(self)
        rect.set_depth(depth)
        rect.set_fill_color(random.choice(COLORS))

        self._win.add(rect)

    def handle_mouse_press(self, event):
        """ Split the current Mondrian rectangles into two either vertically or
            horizontally, based on current split direction. """
        # this gets the location where the mouse clicked
        (x_split, y_split) = event.get_mouse_location()
        if Mondrian.split_direction == "v":
            Mondrian(self._win, self._x_left, x_split, self._y_top, self._y_bottom, self._depth - 1)
            Mondrian(self._win, x_split, self._x_right, self._y_top, self._y_bottom, self._depth - 1)
        elif Mondrian.split_direction == "h":
            Mondrian(self._win, self._x_left, self._x_right, self._y_top, y_split, self._depth - 1)
            Mondrian(self._win, self._x_left, self._x_right, y_split, self._y_bottom, self._depth - 1)


    def handle_key_press(self, event):
        """ Stores whether h or v key was pressed most recently on keyboard. """
        # get the key that was pressed
        key = event.get_key()
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
