# Queen Logic

import pygame as py
from data.classes.piece import Piece

class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'src/data/classes/imgs_pieces/' + color[0] + '_queen.png'
        self.img = py.image.load(img_path)
        self.img = py.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'Q'

    def get_possible_moves(self, board):
        directions = [
            (0, -1),  # North
            (1, -1),  # Northeast
            (1, 0),   # East
            (1, 1),   # Southeast
            (0, 1),   # South
            (-1, 1),  # Southwest
            (-1, 0),  # West
            (-1, -1)  # Northwest
        ]
        
        output = []
        for dx, dy in directions:
            path = []
            x, y = self.x, self.y
            while True:
                x += dx
                y += dy
                if not (0 <= x < 8 and 0 <= y < 8):  # Check board bounds
                    break
                path.append(board.get_square_from_pos((x, y)))
            output.append(path)
        
        return output