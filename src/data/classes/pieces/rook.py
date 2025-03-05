# Rook Logic

import pygame as py
from data.classes.piece import Piece
from data.classes.piece import SCALE

class Rook(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/classes/imgs_pieces/' + color[0] + '_rook.png'
        self.img = py.image.load(img_path)
        self.img = py.transform.scale(self.img, (board.tile_width - SCALE, board.tile_height - SCALE))
        self.notation = 'R'

    # TODO get_possible_moves(self, board):