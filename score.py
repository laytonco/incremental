import pygame
import math
import sys
from helperfunctions import *
from constants import *



class Score:
    def __init__(self, font, size):
        self.score = 0
        self.font = pygame.font.Font(font, size)

    def increase(self, amount=1):
        self.score += amount

    def draw(self, surface):
        formatted_score = format_number(self.score)
        score_per_second = self.score / (pygame.time.get_ticks() / 1000)  # Calculate fragments per second
        formatted_score_per_second = format_number(score_per_second)

        # Render text surfaces
        score_text = self.font.render(f"Fragments: {formatted_score}", True, GRAY)
        score_per_second_text = self.font.render(f"Frags / s: {formatted_score_per_second}", True, GRAY)

        # Positioning
        padding = 10
        x_right = surface.get_width() - score_text.get_width() - padding  # Align to top-right
        y_top = padding  # Start from top

        # Draw text
        surface.blit(score_text, (x_right, y_top))  # Draw "Fragments"
        surface.blit(score_per_second_text, (x_right, y_top + score_text.get_height() + 5))  # Draw "Fragments/s"