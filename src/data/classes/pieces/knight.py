# Knight Logic

import pygame as py
from data.classes.piece import Piece

class Knight(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'src/data/classes/imgs_pieces/' + color[0] + '_knight.png'
        self.img = py.image.load(img_path)
        self.img = py.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'K'

    def get_possible_moves(self, board):
        movements = [
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
            (2, 1),
            (-2, 1),
            (2, -1),
            (-2, -1)
        ]
        output = []
        for dx, dy in movements:
            x, y = self.x, self.y
            if (0 <= x < 8 and 0 <= y < 8):  # Check board bounds
                output.append(board.get_square_from_pos((x, y)))
        return output