import pygame
import math
from helperfunctions import *
from constants import *
from upgradeclickamount import UpgradeClickAmount


class UpgradeMultiplier:
    def __init__(self, font, size, player_square, y_offset, messanger, click_amount):
        self.messanger = messanger
        self.font = pygame.font.Font(font, size)
        self.cost = 50
        self.text = "Multiplier 1.5x"
        self.player_square = player_square  # Reference to the player square
        self.button_rect = pygame.Rect(10, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.click_amount = click_amount

    def draw(self, surface):
        # Draw the white outline
        outline_rect = self.button_rect.inflate(4, 4)
        pygame.draw.rect(surface, (255, 255, 255), outline_rect)
        # Draw the button
        pygame.draw.rect(surface, GRAY, self.button_rect)
        
        # Render the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        surface.blit(text_surface, text_rect)

        # Render the cost
        formatted_cost = format_number(self.cost)
        cost_text = self.font.render(f"Cost: {formatted_cost}", True, (255, 255, 255))
        cost_rect = cost_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top))
        surface.blit(cost_text, cost_rect)

        # Render the current multiplier
        formatted_multiplier = format_number(self.player_square.click_amount / self.click_amount)
        multiplier_text = self.font.render(f"Multiplier: {formatted_multiplier}x", True, (255, 255, 255))
        multiplier_rect = multiplier_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top + 25))
        surface.blit(multiplier_text, multiplier_rect)

    def click(self, x, y):
        if self.button_rect.collidepoint(x, y):
            self.upgrade_size()

    def upgrade_size(self):
        if self.player_square.score.score < self.cost:
            self.messanger.add_message("Not enough fragments!")
            return
        else:
            self.player_square.score.increase(-self.cost)
        new_click_amount = self.player_square.click_amount * 1.5
        self.player_square.click_amount = new_click_amount  # Update the click amount with the new value
        self.cost = int(self.cost * 1.25)# Increase the cost by 50
        print(f"Upgrade! Multiplier is now {new_click_amount}, new cost is {self.cost}")