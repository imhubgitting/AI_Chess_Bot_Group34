# Square Initialization
import pygame as py

class Square:
    # * Setup Functions
    def __init__(square, x, y, width, height):
        # Initializes chessboard tile with (x, y), width/height
        square.x = x
        square.y = y
        square.width = width
        square.height = height
        square.abs_x = x * width
        square.abs_y = y * height
        square.abs_pos = (square.abs_x, square.abs_y)
        square.pos = (x, y)
        square.color = 'light' if (x + y) % 2 == 0 else 'dark'
        square.draw_color = (220, 208, 194) if square.color == 'light' else (53, 53, 53)
        square.highlight_color = (100, 249, 83) if square.color == 'light' else (0, 228, 10)
        square.occupying_piece = None
        square.coord = square.get_coord()
        square.highlight = False
        square.rect = py.Rect(
            square.abs_x,
            square.abs_y,
            square.width,
            square.height
        )
            

    # * Helper Functions
    def get_coord(self):
        # Converts (x, y) to chess notation (e.g. a1, h8, ...) (a-h, 1-8)
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)


    # * Rendering Functions
    def draw(self, display):
        # Draws square with appropriate color, highlighting
        # When a piece is on square, centers and displays piece's image

        # configures if tile should be light or dark or highlighted tile
        if self.highlight:
            py.draw.rect(display, self.highlight_color, self.rect)
        else:
            py.draw.rect(display, self.draw_color, self.rect)
        # adds the chess piece icons
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)

