import pygame
from constants import *

class SizeDisplay:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 36)
        self.current_size = 1  # Initial size value

    def update_size(self, main_block, new_size):
        self.current_size = new_size
        # Increase the size of the main block by 0.01%
        main_block.width *= 1.01
        main_block.height *= 1.01
        main_block.x = (self.screen_width - main_block.width) / 2
        main_block.y = (self.screen_height - main_block.height) / 2

    def draw(self, screen):
        size_text = f"Size: {self.current_size:.2f}"
        text_surface = self.font.render(size_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topright=(self.screen_width - 10, 10))
        screen.blit(text_surface, text_rect)