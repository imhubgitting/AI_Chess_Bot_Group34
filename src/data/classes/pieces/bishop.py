# Bishop Logic

import pygame as py
from data.classes.piece import Piece

class Bishop(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'src/data/classes/imgs_pieces/' + color[0] + '_bishop'
        self.img = py.image.load(img_path)
        self.img = py.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'B'


    def get_possible_moves(self, board):
        directions = [
            (1, -1),  # Northeast
            (1, 1),   # Southeast
            (-1, 1),  # Southwest
            (-1, -1)  # Northwest
        ]

        output = []
        for dx, dy in directions:
            path = []
            x, y = self.x, self.y
            while True:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):
                    break
                path.append(board.get_square_from_pos((x,y)))
            output.append(path)
        return output
