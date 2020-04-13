"""
    car.py
    Darren Strash
    A car that moves when pressing a button!
"""

from cs110graphics import *

WIN_WIDTH = 600
WIN_HEIGHT = 600


class Car(EventHandler):
    """ A car that moves when we click buttons. """

    def __init__(self, win, width, length, cen):
        EventHandler.__init__(self)

        self._win = win
        self._width = width
        self._length = length
        self._center = cen

        self._color = "deeppink"

        self._rect = Rectangle(self._win, self._width, self._length,
                               self._center)
        self._rect.set_fill_color(self._color)
        self._rect.set_border_color("skyblue")
        self._rect.set_depth(6)

        self._right_light_center = (self._center[0] + self._width//3, \
                                    self._center[1] + self._length//4)
        self._right_light = Circle(self._win, self._width//12, self._right_light_center)
        self._right_light.set_depth(5)
        self._right_light.set_fill_color("lightgray")
        self._win.add(self._right_light)

        self._left_light_center = (self._center[0] + self._width//3, \
                                   self._center[1] - self._length//4)
        self._left_light = Circle(self._win, self._width//12, self._left_light_center)
        self._left_light.set_depth(5)
        self._left_light.set_fill_color("lightgray")
        self._win.add(self._left_light)

        self._rect.add_handler(self)
        self._right_light.add_handler(self)
        self._left_light.add_handler(self)
        self._win.add(self._rect)

        #Give the heading / direction car is facing
        # x = 1 means moving right, x = -1 means moving left (0 means not moving in dir)
        # y = 1 means moving down, y = -1 means moving up (0 means not moving in dir)
        self._heading_x = 1
        self._heading_y = 0

    def move(self, direction):
        """ Move car to the right/left 20 pixels."""

        (x, y) = self._center
        if direction == "forward":
            self._center = (x + self._heading_x * 20, y + self._heading_y * 20)
        elif direction == "backward":
            self._center = (x - self._heading_x * 20, y - self._heading_y * 20)

        self._right_light_center = (self._center[0] + self._width//3, \
                                    self._center[1] + self._length//4)
        self._left_light_center = (self._center[0] + self._width//3, \
                                   self._center[1] - self._length//4)

        self._rect.move_to(self._center)
        self._right_light.move_to(self._right_light_center)
        self._left_light.move_to(self._left_light_center)


class Button(EventHandler):
    """ A button that when clicked will make a car move in a given direction. """

    def __init__(self, window, car, radius, center, direction):
        """ Initialize the buttion's attributes. """
        EventHandler.__init__(self)
        self._win = window
        self._car = car
        self._radius = radius
        self._center = center
        self._direction = direction
        self._circle = Circle(self._win, self._radius, self._center)
        self._circle.set_fill_color("lightgray")
        self._win.add(self._circle)
        self._circle.add_handler(self)

    def handle_mouse_press(self, event):
        """ Change the button color and move the car when mouse button pressed. """
        self._circle.set_fill_color("green")
        self._car.move(self._direction)

    def handle_mouse_release(self, event):
        """ Change the button color back when releasing mouse button. """
        self._circle.set_fill_color("lightgray")

def main(win):
    """The main function."""

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    car = Car(win, 100, 40, (100, 500))
    button = Button(win, car, 15, (100,20), "forward")
    button = Button(win, car, 15, (100,70), "backward")

if __name__ == '__main__':
    """When using cs110graphics, replace the usual line with this one:"""
    StartGraphicsSystem(main)
