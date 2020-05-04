"""
    hey_thats_my_fish_v4.py
    May 4, 2020
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
        self._is_present = True

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

    def get_fish(self):
        """ Return the number of fish on this tile. """

        return self._fish

    def get_row(self):
        """ Return the row of the grid where the tile is located. """

        return self._row

    def get_col(self):
        """ Return the column of the grid where the tile is located. """

        return self._col

    def center_from_row_col(self):
        """ Get the center from a particular row and column. """

        center_x = TILE_RADIUS + TILE_DIAMETER * (self._col // 2)
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
        self._is_present = False
        self._win.remove(self._penguin)
        self._win.remove(self._circle)
        self._win.remove(self._text)

    def is_present(self):
        """ Return True if and only if the tile is present on the board. """

        return self._is_present

    def has_penguin(self):
        """ Return if and only if there is a penguin on the tile. """

        return self._has_penguin

    def get_penguin_color(self):
        """ Get the color of the penguin on the tile. """

        return self._penguin_color

    def select(self):
        """ Update the tile so that we know it's been selected by the user. """

        self._circle.set_border_color(self._penguin_color)

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
            row_list = []
            num_cols = 8
            if row % 2 == 1:
                num_cols = 7

            real_col = 0
            for col in range(num_cols):
                if num_cols == 7:
                    row_list.append("This is a fake tile")
                    real_col += 1
                row_list.append(Tile(win, self, row, real_col))
                real_col += 1
                if num_cols == 8:
                    row_list.append("This is a fake tile")
                    real_col += 1
            self._tiles.append(row_list)


        #TODO: Players, different colored penguins, turns
        self._player_colors = ["green", "red"]
        self._num_players = len(self._player_colors)
        self._current_player = 0
        self._current_player_color = self._player_colors[self._current_player]

        self._message_text = Text(self._win,
                          "{} player's turn to place an initial penguin."
                          .format(self._current_player_color),
                          20, (WIN_WIDTH // 2, WIN_HEIGHT - 50))
        self._win.add(self._message_text)

        self._num_penguins = 0
        self._in_initial_phase = True

        #TODO: move penguins, remove the tiles
        #TODO: track score for each player

    def get_current_player_color(self):
        """ Return the color of the current player. """

        return self._current_player_color

    def handle_initial_phase(self, tile):
        """ Place the penguin in the initial phase. """
        if tile.has_penguin() or tile.get_fish() != 1:
            return

        color = self.get_current_player_color()
        tile.add_penguin(color)
        self._num_penguins += 1
        self._current_player = (self._current_player + 1) % self._num_players
        self._current_player_color = self._player_colors[self._current_player]
        self._message_text.set_text(
                        "{} player's turn to place an initial penguin"
                        .format(self._current_player_color))
        self._in_initial_phase = self._num_penguins < PENGUINS_PER_PLAYER * self._num_players
        if not self._in_initial_phase:
            self._click_on_penguin = True
            self._message_text.set_text(
                            "{} player's turn to select a penguin"
                            .format(self._current_player_color))

    def get_offset(self, row_change, col_change):
        """ Return how many indices to move for checking tiles along particular direction. """

        row_offset = 0
        if row_change != 0:
            row_offset = row_change // abs(row_change)

        col_offset = 0
        if col_change != 0:
            col_offset = col_change // abs(col_change)

        if row_offset == 0:
            col_offset *= 2

        return (row_offset, col_offset)

    def is_valid_move(self, tile):
        """ Check if penguin can move to a given tile. """

        current_row = self._tile_with_penguin_to_move.get_row()
        current_col = self._tile_with_penguin_to_move.get_col()
        target_row = tile.get_row()
        target_col = tile.get_col()

        row_change = target_row - current_row
        col_change = target_col - current_col

        if not (abs(row_change) == abs(col_change) or row_change == 0):
            return False

        (row_offset, col_offset) = get_offset(row_change, col_change)

        check_row = current_row + row_offset
        check_col = current_col + col_offset
        while check_row != target_row or check_col != target_col:
            if self._tiles[check_row][check_col].has_penguin() or \
               not self._tiles[check_row][check_col].is_present():
                return False
            check_row += row_offset
            check_col += col_offset

        # Check the target
        if tile.has_penguin() or not tile.is_present():
            return False

        return True

    def handle_move_phase(self, tile):
        """ Handle the moving a penguin, by either selecting, or moving to new tile. """
        if self._click_on_penguin:
            if tile.has_penguin() and self._current_player_color == tile.get_penguin_color():
                tile.select()
                self._tile_with_penguin_to_move = tile
                self._click_on_penguin = False
                self._message_text.set_text(
                                "{} player's turn to move selected penguin"
                                .format(self._current_player_color))
        else:
            if not tile.has_penguin() and self.is_valid_move(tile):
                self._tile_with_penguin_to_move.remove_penguin()
                tile.add_penguin(self._current_player_color)
                self._current_player = (self._current_player + 1) % self._num_players
                self._current_player_color = self._player_colors[self._current_player]
                self._click_on_penguin = True
                self._message_text.set_text(
                                "{} player's turn to select a penguin"
                                .format(self._current_player_color))

    def handle_tile_click(self, tile):
        """ Handle all logic when a tile is clicked. """

        if self._in_initial_phase:
            self.handle_initial_phase(tile)
        else:
            self.handle_move_phase(tile)

        #TODO: Penguins only move in a straight line (along hexagonal grid)
        #TOdO: Penguins can't jump over other penguins or missing tiles.
        #TODO: Keep score
        #TODO: Declare winner.


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    hey = HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """

    StartGraphicsSystem(main)
