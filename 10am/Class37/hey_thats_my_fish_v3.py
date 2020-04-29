"""
    hey_thats_my_fish_v3.py
    April 29, 2020
    Darren Strash and CS 110
    Implementation of Hey That's My Fish!
"""

from cs110graphics import *
import random, math

WIN_WIDTH = 800
WIN_HEIGHT = 800

CIRCLE_DIAMETER = WIN_WIDTH // 8
CIRCLE_RADIUS = CIRCLE_DIAMETER // 2

PENGUIN_RADIUS = 15
NUM_PENGUINS_PER_PLAYER = 2

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

        #get random number of fish
        self._fish = random.randint(1,3)
        self._has_penguin = False
        self._penguin_color = None

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

    def get_fish(self):
        return self._fish

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col

    def get_center_from_row_col(self):
        """ Get the center from a particular row and column. """

        start_x = CIRCLE_RADIUS
        if self._row % 2 == 1:
            start_x = CIRCLE_DIAMETER
        real_x = start_x + CIRCLE_DIAMETER * (self._col // 2)

        start_y = CIRCLE_RADIUS
        real_y = start_y + int(math.sqrt(3) * CIRCLE_RADIUS) * self._row
        return (real_x, real_y)

    def add_penguin(self, color):
        """ Add a penguin to the tile if it doesn't already have one. """

        if not self._has_penguin:
            self._penguin_color = color
            self._penguin = Circle(self._win, PENGUIN_RADIUS, self._center)
            self._penguin.add_handler(self)
            self._penguin.set_depth(25)
            self._penguin.set_fill_color(color)
            self._win.add(self._penguin)
            self._has_penguin = True

    def remove_penguin(self):
        """ Remove the tile from the board. """

        self._win.remove(self._circle)
        self._win.remove(self._text)
        self._win.remove(self._penguin)
        self._has_penguin = False

    def has_penguin(self):
        """ Determine if the tile has a penguin. """

        return self._has_penguin

    def get_penguin_color(self):
        """ Get penguin's color. """

        return self._penguin_color

    def handle_mouse_press(self, event):
        """ Add a green penguin when clicking the tile. """
        
        self._board.handle_tile_click(self, self._row, self._col)

    def select(self):
        self._circle.set_border_color(self._penguin_color)


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

            real_col = 0

            for col in range(num_cols):
                if num_cols == 7:
                    row_list.append(None)
                    real_col += 1
                row_list.append(Tile(win, self, row, real_col))
                real_col += 1
                if num_cols == 8:
                    row_list.append(None)
                    real_col += 1

            self._tiles.append(row_list)

        #need a notion of a player / penguin color
        self._player_colors = ["green", "red"]
        self._num_players = len(self._player_colors)
        self._current_player = 0
        self._current_player_color = self._player_colors[self._current_player]

        #need to place penguins in one phase, and move them in another.
        self._in_initial_phase = True

        self._text = Text(self._win,
                          "{} player's turn to place an initial penguin"
                          .format(self._current_player_color), 30,
                          (WIN_WIDTH // 2, WIN_HEIGHT - 50))
        self._win.add(self._text)

        self._num_penguins = 0
        self._tile_with_current_penguin = None

        #TODO: need to keep score
        #TODO: fix moving logic (move along rows and diagonals)
        #TODO: end game?

    def get_current_player_color(self):
        """ Get current player color. """

        return self._current_player_color

    def handle_initial_turn(self, tile):
        """ Handle logic for initial penguin placement. """
        color = self.get_current_player_color()
        if tile.has_penguin() or tile.get_fish() != 1:
            return
        tile.add_penguin(color)

        self._num_penguins += 1
        self._current_player = (self._current_player + 1) % len(self._player_colors)
        self._current_player_color = self._player_colors[self._current_player]
        self._text.set_text("{} player's turn to place an initial penguin"
        .format(self._current_player_color))

        if self._num_penguins == self._num_players * NUM_PENGUINS_PER_PLAYER:
            self._in_initial_phase = False
            self._select_penguin = True
            self._text.set_text("{} player's turn to select a penguin"
            .format(self._current_player_color))

    def handle_penguin_move(self, tile):
        """ Handle selecting and moving penguins. """
        if self._select_penguin:
            if tile.has_penguin() and tile.get_penguin_color() == self._current_player_color:
                tile.select()
                self._tile_with_current_penguin = tile
                self._select_penguin = False
                self._text.set_text("{} player's turn to move selected penguin"
                .format(self._current_player_color))

        else:
            if not tile.has_penguin() and self.valid_move(tile):
                tile.add_penguin(self._current_player_color)
                self._tile_with_current_penguin.remove_penguin()
                self._select_penguin = True
                self._current_player = (self._current_player + 1) % len(self._player_colors)
                self._current_player_color = self._player_colors[self._current_player]
                self._text.set_text("{} player's turn to select a penguin"
                .format(self._current_player_color))

    def valid_move(self, tile):
        """ Check if the selected penguin can move to the given tile. """
        current_row = self._tile_with_current_penguin.get_row()
        current_col = self._tile_with_current_penguin.get_col()
        target_row = tile.get_row()
        target_col = tile.get_col()

        # Currently only detects if penguins between current and target,
        # and only checks row in forward order
        # TODO: Handle backward order
        if current_row == target_row:
            for col in range(current_col + 2, target_col + 1, 2):
                if self._tiles[current_row][col].has_penguin():
                    return False

        #TODO: handle diagonal movement

        return True


    def handle_tile_click(self, tile, row, col):
        """ Handle all game logic when clicking a tile. """

        if self._in_initial_phase:
            self.handle_initial_turn(tile)
        else:
            self.handle_penguin_move(tile)


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    hey = HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """

    StartGraphicsSystem(main)
