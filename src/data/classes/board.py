# Board Initialization

import pygame as py
from data.classes.square import Square
from data.classes.pieces.rook import Rook
from data.classes.pieces.knight import Knight
from data.classes.pieces.bishop import Bishop
from data.classes.pieces.queen import Queen
from data.classes.pieces.king import King
from data.classes.pieces.pawn import Pawn

class Board:
# * Setup Functions
    def __init__(self, width, height):
        # Initializes board given width and height
        # Sets up tile size
        # Initializes game state
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        # Creates 8x8 grid of Square objects
        output = []
        for y in range(8):
            for x in range(8):
                output.append(
                    Square(x, y, self.tile_width, self.tile_height)
                )
        return output

# TODO set up each piece's __init__
    def setup_board(self):
        # Uses self.config to place pieces on their correct squares
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece[1] == 'R':
                        square.occupying_piece = Rook(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece[1] == 'N':
                        square.occupying_piece = Knight(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'B':
                        square.occupying_piece = Bishop(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'K':
                        square.occupying_piece = King(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'P':
                        square.occupying_piece = Pawn(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                        


# * Helper Functions
    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece



# * Game Logic
    def handle_click(self, mx, my):
        # Handles user clicks on board

        # Convert mouse coords into board positions
        x = mx // self.tile_width
        y = my // self.tile_height

        # Get board square that was clicked
        clicked_square = self.get_square_from_pos((x,y))
        
        # If no piece is currently selected
        if self.selected_piece is None:
            # Check if clicked square has a piece
            if clicked_square.occupying_piece is not None:
                # Select piece on that square
                self.selected_piece = clicked_square.occupying_piece

        # If a piece is already selected, attempt to move it        
        elif self.selected_piece.move(self, clicked_square):
            # If move is successful, switch turn to other player
            self.turn = 'white' if self.turn == 'black' else 'black'
        
        # If move was not successful, check if clicked square contains another piece
        elif clicked_square.occupying_piece is not None:
            # Allow player to reselect a different piece if it's theirs
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece

    # TODO def is_in_check(self, color, board_change=None):
        # Checks if given color's king is in check 

    # TODO def is_in_checkmate(self, color):
        # Check if king has any valid moves, if not, checkmate is true

# * Rendering
    def draw(self, display):
        # Draws board and highlights selected piece and its valid moves

        # Check if there is a currently selected piece
        if self.selected_piece is not None:
            # Highlight square where selected piece is located
            self.get_square_from_pos(self.selected_piece.pos).highlight = True

            # Get all valid moves for selected piece and highlight those moves
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True

        # Loop through all squares on board and draw them
        for square in self.squares:
            square.draw(display)
