# Queen Logic

import pygame as py
from dataclasses import Piece

class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/imgs/' + color[0] + '_queen.png'
        self.img = py.image.load(img_path)
        self.img = py.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'Q'

# TODO get_possible_moves(self, board):