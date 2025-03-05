# Pawn Logic

import pygame as py
from data.classes.piece import Piece
from data.classes.piece import SCALE

class Pawn(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = 'data/classes/imgs_pieces/' + color[0] + '_pawn.png'
        self.img = py.image.load(img_path)
        self.img = py.transform.scale(self.img, (board.tile_width - SCALE, board.tile_height - SCALE))
        self.notation = 'P'

    def get_possible_moves(self, board):
        direction = -1 if self.color == 'white' else 1  # White moves up (-1), Black moves down (+1)
        moves = [(0, direction)]  # Normal forward move

        if not self.has_moved:
            moves.append((0, 2 * direction))  # Double move on first move

        # Capture diagonally
        captures = [(-1, direction), (1, direction)]

        output = []
        x, y = self.x, self.y

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                square = board.get_square_from_pos((new_x, new_y))
                if square and square.occupying_piece is None:  # Move only if square is empty
                    output.append(square)

        for dx, dy in captures:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                square = board.get_square_from_pos((new_x, new_y))
                if square and square.occupying_piece is not None and square.occupying_piece.color != self.color:
                    output.append(square)

        return output