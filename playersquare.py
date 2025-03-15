import pygame
import math
import sys
from floatingtext import FloatingText

# Define the square object
class PlayerSquare:
    def __init__(self, color, size, score):
        try:
            self.image = pygame.image.load('images/playersquare.png')
            self.image = pygame.transform.scale(self.image, (size, size))
        except FileNotFoundError:
            print("Image file not found. Creating a placeholder image.")
            self.image = pygame.Surface((size, size))
            self.image.fill(color)
        self.color = color
        self.size = size
        self.rect = self.image.get_rect(center=(1280 // 2, 720 // 2))
        self.score = score
        self.click_amount = 1  # Initial click amount
        self.floating_texts = []
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        self.floating_texts = [text for text in self.floating_texts if text.draw(surface)]

    def click(self, x=None, y=None):
        if x is None and y is None or self.rect.collidepoint(x, y):
            self.score.increase(self.click_amount)
            if x is not None and y is not None:
                self.floating_texts.append(FloatingText(self.click_amount, (x, y), self.font))

    def hit_by_projectile(self, x, y):
        self.score.increase(self.click_amount)
       # Update cracks when hit by projectile
        self.floating_texts.append(FloatingText(self.click_amount, (x, y), self.font))

