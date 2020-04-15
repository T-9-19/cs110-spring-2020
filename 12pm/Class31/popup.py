
from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

class Counter(EventHandler):
    """ Make a button that displays the numbe of times it has been clicked
        Every 5 times you click it, a popup will appear with the given message. """

    def __init__(self, win, center, message):
        """ Initialize the counter's shape, text, and its use as an EventHandler. """
        EventHandler.__init__(self)

        self._win = win
        self._center = center
        self._message = message

        self._count = 0
        self._clickable = True

        self._circ = Circle(self._win, 75, center)
        self._circ.set_fill_color("gold")
        self._circ.set_depth(50)
        self._circ.add_handler(self)
        self._win.add(self._circ)

        # A graphical object representing text: init with string, font size
        # and center point
        self._text = Text(self._win, str(self._count), 20, center)
        self._text.set_depth(20)
        self._text.add_handler(self)
        self._win.add(self._text)


    def handle_mouse_press(self, event):
        """ If the counter can currently be clicked, increase the counter and
            display the new count. If clicked 5 times, popup a message. """
        if self._clickable:
            self._count += 1
            self._text.set_text(str(self._count))

            if self._count % 5 == 0:
                self.toggle_clickable()
                Popup(self._win, self, (WIN_WIDTH // 2, WIN_HEIGHT // 2), self._message)

    def toggle_clickable(self):
        """ If the counter is clickable, make it not clickable; if it's not clickable,
            make it clickable. """
        self._clickable = not self._clickable

class Popup(EventHandler):
    """ Makes a popup window that lets you click a "close" button. """

    #class variable: a variable is accessible to every instance of the class
    #You access it with Popup.popup_depth
    popup_depth = 10

    def __init__(self, win, counter, center, message):
        """ Initialize the popup window's shape, button, message, and use the
            present object as an EventHandler. """
        EventHandler.__init__(self)
        self._win     = win
        self._counter = counter
        self._center  = center
        self._message = message

        #make a rectangle
        #Things to consider: smaller than current window
        self._popup_window = Rectangle(self._win, 250, 150, self._center)
        self._popup_window.set_depth(Popup.popup_depth)
        Popup.popup_depth -= 1
        self._popup_window.set_fill_color("tomato")
        self._win.add(self._popup_window)

        (x,y) = self._center

        #have text on popup
        self._text = Text(self._win, self._message, 20, (x, y - 20))
        self._win.add(self._text)
        self._text.set_depth(Popup.popup_depth)
        Popup.popup_depth -= 1

        #some kind of button to make popup disappear
        # x in corner, or OK button.
        self._button = Rectangle(self._win, 100, 30, (x, y + 40))
        self._button.set_depth(Popup.popup_depth)
        Popup.popup_depth -= 1
        self._win.add(self._button)

        self._button_text = Text(self._win, "Go away!", 15, (x, y + 40))
        self._button_text.set_depth(Popup.popup_depth)
        Popup.popup_depth -= 1
        self._win.add(self._button_text)

        self._button.add_handler(self)
        self._button_text.add_handler(self)

    def handle_mouse_press(self, event):
        """ When clicking the button, make the counter clickable again and
            remove the popup from the window. """
        self._counter.toggle_clickable()
        self._win.remove(self._popup_window)
        self._win.remove(self._text)
        self._win.remove(self._button)
        self._win.remove(self._button_text)



def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    Counter(win, (200, 200), "This is the\nfirst counter!")
    Counter(win, (400, 400), "This is the\nsecond counter!")


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
