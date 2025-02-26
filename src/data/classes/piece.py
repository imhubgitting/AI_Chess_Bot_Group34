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
    def get_moves(self, board):
        # Returns list of possible moves
        output = []
        for direction in self.get_possible_moves(board): # TODO write all possible moves for every piece in their .py
                for square in direction:
                    if square.occupying_piece is not None:
                        if square.occupying_piece.color == self.color:
                            break
                        else:
                            output.append(square)
                            break
                    else:
                        output.append(square)
        return output

    def get_valid_moves(self, board):
        # Filters moves from get_moves() 
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        return output


# * Moving Piece Functions
    # TODO move(self, board, square, force=False):
        # Pawn Promotion

        # Move rook if castles


# * Attack Calculation Functions
    def attacking_squares(self, board):
        # Returns squares the piece is attacking
        return self.get_moves(board)
