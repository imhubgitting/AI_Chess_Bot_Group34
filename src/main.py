# Game Loop

import pygame

pygame.init()

WINDOW_SIZE = (600,600)
screen = pygame.display.set_mode(WINDOW_SIZE)

def draw(screen):
    screen.fill('white')
    pygame.display.update()
    
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)
        