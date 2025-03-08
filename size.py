import pygame
from constants import *


class SizeDisplay:
    def __init__(self, screen_width, screen_height):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.font = pygame.font.Font(None, 36)
        self.current_size = 1  # Initial size value

    def update_size(self, new_size):
        self.current_size = new_size

    def draw(self, screen):
        size_text = f"Size: {self.current_size}"
        text_surface = self.font.render(size_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topright=(self.screen_width - 10, 10))
        screen.blit(text_surface, text_rect)