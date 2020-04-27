"""
    hey_thats_my_fish_v2.py
    April 27, 2020
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

PENGUINS_PER_PLAYER = 2

class Tile(EventHandler):
    """ A class to represent a tile in the game Hey That's My Fish! """

    def __init__(self, win, board, row, col):
        """ Construct the tile, placing it into correct position based on its
            row and column, and give it a random number of fish. """

        EventHandler.__init__(self)
        self._win = win
        self._board = board
        self._row = row
        self._col = col

        self._has_penguin = False

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

        self._has_penguin = True
        self._penguin_color = color
        self._penguin = Circle(self._win, PENGUIN_RADIUS, self._center)
        self._penguin.set_depth(25)
        self._penguin.set_fill_color(color)
        self._penguin.add_handler(self)
        self._win.add(self._penguin)

    def remove_penguin(self):
        """ Remove's penguin from the tile and tile from the board. """

        self._has_penguin = False
        self._win.remove(self._penguin)
        self._win.remove(self._circle)
        self._win.remove(self._text)

    def has_penguin(self):
        """ Return if there is a penguin on the tile. """

        return self._has_penguin

    def get_penguin_color(self):
        """ Get the color of the penguin on the tile. """

        return self._penguin_color

    def handle_mouse_press(self, event):
        """ Add a green penguin when clicking the tile. """

        self._board.handle_tile_click(self)


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
                self._row_list.append(Tile(win, self, row, col))

        #TODO: Players, different colored penguins, turns
        self._player_colors = ["green", "red"]
        self._num_players = len(self._player_colors)
        self._current_player = 0
        self._current_player_color = self._player_colors[self._current_player]

        self._text = Text(self._win,
                          "Player {}'s turn to place an initial penguin."
                          .format(self._current_player + 1),
                          20, (WIN_WIDTH // 2, WIN_HEIGHT - 50))
        self._win.add(self._text)

        self._num_penguins = 0
        self._in_initial_phase = True

        #TODO: move penguins, remove the tiles
        #TODO: track score for each player

    def get_current_player_color(self):
        """ Return the color of the current player. """

        return self._current_player_color

    def handle_tile_click(self, tile):
        """ Handle all logic when a tile is clicked. """
        # placing initial penguins
        if self._in_initial_phase:
            #if the tile has a penguin already, do nothing
            if tile.has_penguin():
                return

            color = self.get_current_player_color()
            tile.add_penguin(color)
            self._num_penguins += 1
            self._current_player = (self._current_player + 1) % self._num_players
            self._current_player_color = self._player_colors[self._current_player]
            self._text.set_text("Player {}'s turn to place an initial penguin".format(self._current_player + 1))
            self._in_initial_phase = self._num_penguins < PENGUINS_PER_PLAYER * self._num_players
            if not self._in_initial_phase:
                self._click_on_penguin = True
        else:
            #otherwise, moving penguins to new tile
            #first select penguin we want to move
            if self._click_on_penguin:
                if tile.has_penguin() and self._current_player_color == tile.get_penguin_color():
                    self._tile_with_penguin_to_move = tile
                    self._click_on_penguin = False
            else:
                if not tile.has_penguin():
                    self._tile_with_penguin_to_move.remove_penguin()
                    tile.add_penguin(self._current_player_color)
                    self._current_player = (self._current_player + 1) % self._num_players
                    self._current_player_color = self._player_colors[self._current_player]
                    self._click_on_penguin = True

            pass


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    hey = HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """

    StartGraphicsSystem(main)
