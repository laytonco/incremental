import pygame
from constants import *
import sys
from mainblock import MainBlock

def main():
    pygame.init()

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 780

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Idle square")

    x0 = (SCREEN_WIDTH - RECT_WIDTH) / 2
    y0 = (SCREEN_HEIGHT - RECT_HEIGHT) / 2

    # frames per second
    clock = pygame.time.Clock()

    # main block character
    main_block = MainBlock(x0, y0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_block.handle_event(event)

        screen.fill("black")
        main_block.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()