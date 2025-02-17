# Piece Initialization
import pygame as py

class Piece:
    # * Setup Functions
        def __init__(self, pos, color, board):
        # Initializes generic piece with its pos, color, and reference to board
            self.pos = pos
            self.x = pos[0]
            self.y = pos[1]
            self.color = color
            self.has_moved = False


    # * Move Generation Functions
        # TODO get_moves(self, board):
            # Returns list of possible moves

        # TODO get_valid_moves(self, board):
            # Filters moves from get_moves() 


    # * Moving Piece Functions
        # TODO move(self, board, square, force=False):
            # Pawn Promotion

            # Move rook if castles


    # * Attack Calculation Functions
        # TODO attacking_squares(self, board):
            # Returns squares the piece is attacking
