# Board Initialization

import pygame as py
from data.classes.square import Square
from data.classes.pieces.queen import Queen

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
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece[1] == 'N':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'B':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'K':
                        square.occupying_piece = Queen(
                            (x, y), 'white' if piece[0] == 'w' else 'black', self
                        )
                    elif piece[1] == 'P':
                        square.occupying_piece = Queen(
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
        # Convert mouse coordinates to board grid position
        print("handle_click triggered!")
        x = mx // self.tile_width
        y = my // self.tile_height
        print("Computed grid position:", x, y)
        clicked_square = self.get_square_from_pos((x,y))
        print(f"Clicked square: ({clicked_square.x}, {clicked_square.y})")
        # If a piece is selected already, try to move it
        if self.selected_piece:
            valid_moves = self.selected_piece.get_valid_moves(self)
            if clicked_square in valid_moves:
                #Move the piece to the clicked square
                self.selected_piece.move(self, clicked_square)
                self.selected_piece = None # Deselect
                # Toggle turn
                self.turn = 'black' if self.turn == 'white' else 'white'
            else:
                # If piece is another piece of current turn then just switch to that piece
                if clicked_square.occupying_piece and clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece
                else:
                    self.selected_piece = None #Invalid move
        else:
            # If nothing currently sleected, select a piece if it is current players piece
            if clicked_square.occupying_piece and clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece


    def is_in_check(self, color, board_change=None):
    # Temporary just to run and test other functionality, until full check logic is implemented.
        return False

    # TODO def is_in_checkmate(self, color):
        # Check if king has any valid moves, if not, checkmate is true

# * Rendering
    def draw(self, display):
        # Draws board and highlights selected piece and its valid moves
        if self.selected_piece is not None:
            self.get_square_from_pos(self.selected_piece.pos).highlight = True
            for square in self.selected_piece.get_valid_moves(self):
                square.highlight = True
        for square in self.squares:
            square.draw(display)


