# Piece Initialization
import pygame as py

SCALE = 15

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

        # Get possible moves (may be different for each piece)
        possible_moves = self.get_possible_moves(board)

        # Ensure we handle different formats (list of lists for multi-paths like Queen, Rook, etc.)
        if isinstance(possible_moves, list) and isinstance(possible_moves[0], list):
            move_sets = possible_moves  # Multi-path pieces (Queen, Rook, etc.)
        else:
            move_sets = [possible_moves]  # Single list pieces (Pawn, Knight)
                

        for direction in move_sets:
            for square in direction:
                if square.occupying_piece is not None:
                    if square.occupying_piece.color == self.color:
                        break
                    else:
                        output.append(square) # Enemy piece can be attacked
                        break
                else:
                    output.append(square) # Empty square can be moved to
        return output

    def get_valid_moves(self, board):
        # Filters moves from get_moves() 
        output = []
        for square in self.get_moves(board):
            # TODO if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
            output.append(square)
        return output


# * Moving Piece Functions
    def move(self, board, square, force=False):
        for i in board.squares:
            i.highlight = False
        if square in self.get_valid_moves(board) or force:
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = None
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
        else:
            board.selected_piece = None
            return False
        # TODO Pawn Promotion

        # TODO Move rook if castles


# * Attack Calculation Functions
    def attacking_squares(self, board):
        # Returns squares the piece is attacking
        return self.get_moves(board)
