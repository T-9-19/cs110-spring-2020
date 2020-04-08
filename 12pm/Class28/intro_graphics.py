"""
    File: intro_graphics.py
    Author: Darren Strash
    Description: Introduction to cs110graphics.
"""
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

from cs110graphics import *

class Light(EventHandler):
    """ A  circular "light" that changes color when clicked. Must be a child
        class of EventHandler in order to handle events! """

    def __init__(self, window, radius, center_point):
        """ Construct the Light by constructing the parent class and creating
            the circle and assigning the present object to be its event handler."""
        EventHandler.__init__(self)
        self._window = window
        self._radius = radius
        self._center = center_point

        self._circle = Circle(window, radius, center_point)

        # Be sure to add our Light object as the handler for the circle. Then
        # when circle receives events, the Light object self will handle them.
        self._circle.add_handler(self)
        window.add(self._circle)

        self._colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        self._color_index = 0
        self._circle.set_fill_color(self._colors[self._color_index])

    def handle_mouse_press(self, event):
        """ Override the EventHandler method handle_mouse_press to change
            the color of the circle. """
        self._color_index = (self._color_index + 1) % len(self._colors)
        self._circle.set_fill_color(self._colors[self._color_index])

class Light2(Light):
    """ A circular "light" that changes between earthtone colors when
        clicked. """

    def __init__(self, window, radius, center_point):
        """ Construct the parent Light object (which initializes the attributes
            and creates the colored circle. Then create a new list of colors.
            And set the color of the circle to be in our new palette."""
        Light.__init__(self, window, radius, center_point)
        self._colors = ["black", "brown", "tan", "white"]
        self._circle.set_fill_color(self._colors[self._color_index])


def main(window):
    """ For cs110graphics projects, main takes a Window object as a parameter. """

    # set window dimensions
    window.set_width(WINDOW_WIDTH)
    window.set_height(WINDOW_HEIGHT)

    # 1. making a circle
    radius = 40
    center_point = (0,0)
    first_circle = Circle(window, radius, center_point)
    first_circle.set_fill_color("pink")
    first_circle.set_border_color("blue")
    window.add(first_circle)

    # 2. make a "light", a circle that changes color when you click it with mouse
    light = Light(window, 30, (60, 100))
    light2 = Light(window, 10, (300, 300))

    # 3. make a new light that rotates through earthtones.
    new_light = Light2(window, 60, (400, 200))

if __name__ == "__main__":
    """ We will now call this when we use cs110graphics. """
    StartGraphicsSystem(main)
