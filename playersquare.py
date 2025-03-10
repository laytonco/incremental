import pygame
import math
import sys

# Define the square object
class PlayerSquare:
    def __init__(self, color, size, score):
        self.color = color
        self.size = size
        self.rect = pygame.Rect((1280 - size) // 2, (700 - size) // 2, size, size)
        self.score = score
        self.click_amount = 1  # Initial click amount

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def click(self, x=None, y=None):
        if x is None and y is None or self.rect.collidepoint(x, y):
            self.score.increase(self.click_amount)