import pygame
import math 
from helperfunctions import *
from constants import *

class FloatingText:
    def __init__(self, text, position, font, color=(255, 255, 255), duration=1000):
        if isinstance(text, (int, float)):
            self.text = format_number(text)
        else:
            self.text = text
        self.position = position
        self.font = font
        self.color = color
        self.duration = duration
        self.creation_time = pygame.time.get_ticks()

    def draw(self, surface):
        elapsed_time = pygame.time.get_ticks() - self.creation_time
        if elapsed_time < self.duration:
            alpha = max(0, 255 - (255 * elapsed_time / self.duration))
            text_surface = self.font.render(self.text, True, self.color)
            text_surface.set_alpha(alpha)
            surface.blit(text_surface, self.position)
            return True
        return False

