import pygame
import sys
from constants import *

class UpgradeApp:
    def __init__(self, size_display):
        self.size_display = size_display
        self.font = pygame.font.Font(None, 36)
        self.button_rect = pygame.Rect(10, 10, 120, 60)  # Adjusted size for better text fit

    def draw(self, screen):
        # Draw the white outline
        outline_rect = self.button_rect.inflate(4, 4)  # Inflate the rect to create an outline
        pygame.draw.rect(screen, (255, 255, 255), outline_rect)

        # Draw the button
        pygame.draw.rect(screen, (0, 0, 0), self.button_rect)
        text_surface = self.font.render("Upgrade", True, (255, 255, 255))
        
        # Center the text within the button
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event, main_block):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.upgrade_click_amount(main_block)

    def upgrade_click_amount(self, main_block):
        main_block.click_amount = round(main_block.click_amount * 1.3, 2)
        print(f"Upgrade! Click amount is now {main_block.click_amount}")


