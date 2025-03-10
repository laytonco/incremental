import pygame
import math
from constants import *
from helperfunctions import *

class Messanger:
    def __init__(self, font, size):
        self.messages = []

    def add_message(self, message, duration=2000):
        self.messages.append((message, pygame.time.get_ticks(), duration))
    
    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        font = pygame.font.Font(None, 36)
        margin = 20
        spacing = 30

        # Start drawing from the bottom of the screen
        y_position = screen.get_height() - margin

        # Filter out messages that have expired
        self.messages = [(text, start_time, duration) for text, start_time, duration in self.messages if current_time - start_time < duration]

        for text, start_time, duration in reversed(self.messages):
            rendered_text = font.render(text, True, (255, 255, 255))
            text_x = screen.get_width() - rendered_text.get_width() - margin
            y_position -= rendered_text.get_height() + spacing  # Move up message
            screen.blit(rendered_text, (text_x, y_position))
       