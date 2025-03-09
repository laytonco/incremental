import pygame
from constants import *

class FloatingText:
    def __init__(self, x, y, click_amount):
        self.click_amount = click_amount
        self.x = x
        self.y = y
        self.alpha = 255

    def draw(self, screen, click_amount):
        # Format the click_amount to 2 decimal places
        current_score_rate_text = f"+{click_amount:.2f}"
        font = pygame.font.Font(None, 36)
        text = font.render(current_score_rate_text, True, (255, 255, 255))
        text.set_alpha(self.alpha)
        screen.blit(text, (self.x, self.y))
        self.y -= 1
        self.alpha -= 2
