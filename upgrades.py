import pygame
import sys

import pygame

class UpgradeApp:
    def __init__(self):
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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.upgrade()

    def upgrade(self):
        print("Upgrade button clicked!")