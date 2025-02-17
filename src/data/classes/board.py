# Board Initialization

import pygame as py

# TODO class Board:
# * Setup Functions
    # TODO def __init__(self, width, height):
        # Initializes board given width and height
        # Sets up tile size
        # Initializes game state

    # TODO def generate_squares(self):
        # Creates 8x8 grid of Square objects

    # TODO def setup_board(self):
        # Uses self.config to place pieces on their correct squares


# * Helper Functions
    # TODO def get_square_from_pos(self, pos):
        # Returns Square object given (x, y)

    # TODO def get_piece_from_pos(self, pos):
        # Returns piece occupying square given (x, y)


# * Game Logic
    # TODO def handle_click(self, mx, my):
        # Handles user clicks on board

    # TODO def is_in_check(self, color, board_change=None):
        # Checks if given color's king is in check 

    # TODO def is_in_checkmate(self, color):
        # Check if king has any valid moves, if not, checkmate is true

# * Rendering
    # TODO def draw(self, display):
        # Draws board and highlights selected piece and its valid moves
