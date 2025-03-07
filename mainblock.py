import pygame
from constants import *

class MainBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def draw(self, screen):
        pygame.draw.rect(screen, ("gray"), (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))