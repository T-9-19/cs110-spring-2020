"""
    car2.py
    Darren Strash
    A car that moves when pressing buttons!
"""

from cs110graphics import *

WIN_WIDTH = 600
WIN_HEIGHT = 600

BUTTON_RADIUS = 15
BUTTON_COLOR = "lightgray"


class Car(EventHandler):
    """ A car that moves when we click buttons. """

    def __init__(self, win, color, width, length, cen):
        EventHandler.__init__(self)

        self._win = win
        self._width = width
        self._length = length
        self._center = cen

        self._color = color
        self._distance = 30

        self._body = Rectangle(self._win, self._width, self._length,
                               self._center)
        self._body.set_fill_color(self._color)
        self._body.set_depth(6)

        right_light_center = (self._center[0] + self._width//3, \
                              self._center[1] + self._length//4)
        self._right_light = Circle(self._win, self._width//12, right_light_center)
        self._right_light.set_depth(5)
        self._right_light.set_fill_color("lightgray")
        self._win.add(self._right_light)

        left_light_center = (self._center[0] + self._width//3, \
                             self._center[1] - self._length//4)
        self._left_light = Circle(self._win, self._width//12, left_light_center)
        self._left_light.set_depth(5)
        self._left_light.set_fill_color("lightgray")
        self._win.add(self._left_light)

        self._body.add_handler(self)
        self._right_light.add_handler(self)
        self._left_light.add_handler(self)
        self._win.add(self._body)

        self._components = [self._body, self._right_light, self._left_light]

        #Give the heading / direction car is facing
        # x = 1 means moving right, x = -1 means moving left (0 means not moving in dir)
        # y = 1 means moving down, y = -1 means moving up (0 means not moving in dir)
        self._heading_x = 1
        self._heading_y = 0


    """
        A brief note on turning: when turning right, y = new

          (x,y) = (0,-1)
                ^
    (-1, 0) <       > (1,0)
                v
              (0, 1)
    """

    def move(self, direction):
        """ Move car forward/backward a custom distance."""

        change_x = 0
        change_y = 0
        if direction == "forward":
            change_x = self._heading_x * self._distance
            change_y = self._heading_y * self._distance

            for component in self._components:
                component.move(change_x, change_y)
        elif direction == "backward":
            change_x = - self._heading_x * self._distance
            change_y = - self._heading_y * self._distance
            
            for component in self._components:
                component.move(change_x, change_y)
        elif direction == "left":
            pivot = self._body.get_pivot()
            new_heading_x = self._heading_y
            new_heading_y = self._heading_x * -1
            self._heading_y = new_heading_y
            self._heading_x = new_heading_x

            for component in self._components:
                component.set_pivot(pivot)
                component.rotate(90)
        elif direction == "right":
            pivot = self._body.get_pivot()
            new_heading_x = -1 * self._heading_y
            new_heading_y = self._heading_x
            self._heading_y = new_heading_y
            self._heading_x = new_heading_x

            for component in self._components:
                component.set_pivot(pivot)
                component.rotate(270)

    def move_forward(self):
        self.move("forward")

    def move_backward(self):
        self.move("backward")

    def turn_left(self):
        self.move("left")

    def turn_right(self):
        self.move("right")


class Button(EventHandler):
    """ A button that when clicked will make a car move in a given direction. """

    def __init__(self, window, trigger, radius, color, center):
        """ Initialize the button's attributes. """
        EventHandler.__init__(self)
        self._win = window
        self._trigger = trigger
        self._radius = radius
        self._center = center
        self._color = color
        self._circle = Circle(self._win, self._radius, self._center)
        self._circle.set_fill_color(self._color)
        self._win.add(self._circle)
        self._circle.add_handler(self)

    def handle_mouse_press(self, event):
        """ Change the button color and move the car when mouse button pressed. """
        self._circle.set_fill_color("green")
        self._trigger()

    def handle_mouse_release(self, event):
        """ Change the button color back when releasing mouse button. """
        self._circle.set_fill_color(self._color)

def main(win):
    """The main function."""

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    car = Car(win, "yellow", 100, 40, (100, 500))

    forward_button  = Button(win, car.move_forward, BUTTON_RADIUS, BUTTON_COLOR, (100,20))
    backward_button = Button(win, car.move_backward, BUTTON_RADIUS, BUTTON_COLOR, (100,70))
    left_button     = Button(win, car.turn_left, BUTTON_RADIUS, BUTTON_COLOR, (75,45))
    right_button    = Button(win, car.turn_right, BUTTON_RADIUS, BUTTON_COLOR, (125,45))

if __name__ == '__main__':
    """When using cs110graphics, replace the usual line with this one:"""
    StartGraphicsSystem(main)
