# Game Loop

import pygame as py

py.init()

WINDOW_SIZE = (600,600)
screen = py.display.set_mode(WINDOW_SIZE)

def draw(screen):
    screen.fill('white')
    py.display.update()
    
if __name__ == '__main__':
    running = True
    while running:
        mx, my = py.mouse.get_pos()

        # * Event Handling
        for event in py.event.get():
            # Quit the game if the user presses the close button
            if event.type == py.QUIT:
                running = False

        # * Checkmate Handling
            # TODO if board.is_in_checkmate('black'):
            # TODO if board.is_in_checkmate('white'):

        # * Draw Handling
        draw(screen)
        