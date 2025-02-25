# Board Initialization

import pygame as py
import Square

class Board:
# * Setup Functions
    def __init__(self, width, height):
        # Initializes board given width and height
        # Sets up tile size
        # Initializes game state
        self.width = width
        self.height = height
        self.title_width = width // 8
        self.title_height = height // 8
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
                    Square(x, y, self.title_width, self.title_height)
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
        return self.squares[pos.x][pos.y]

    def get_piece_from_pos(self, pos):
        square = get_square_from_pos(pos)
        return square.occupying_piece



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
