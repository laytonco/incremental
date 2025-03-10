import pygame
import math
from helperfunctions import *
from constants import * 


class UpgradeClickAmount:
    def __init__(self, font, size, player_square, messanger, click_amount):
        self.click_amount = click_amount
        self.messanger = messanger
        self.font = pygame.font.Font(font, size)
        self.cost = 50
        self.text = "Click +1"
        self.player_square = player_square  # Reference to the player square
        self.button_rect = pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)

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

         # Render the click amount
        formatted_click_amount = format_number(self.click_amount)
        click_amount_text = self.font.render(f"Click amount: {formatted_click_amount}", True, (255, 255, 255))
        click_amount_rect = click_amount_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top + 25))
        surface.blit(click_amount_text, click_amount_rect)
        
        
    def click(self, x, y):
        if self.button_rect.collidepoint(x, y):
            self.upgrade_click_amount()

    def draw_message(self, scren):
        if self.message:
            elapsed_time = pygame.time.get_ticks() - self.message_start_time
            if elapsed_time < self.message_duration:
                font = pygame.font.Font(None, 36)
                text = font.render(self.message, True, (255, 255, 255))
                margin = 20
                text_x = screen.get_width() - text.get_width() - margin
                text_y = screen.get_height() - text.get_height() - margin
                screen.blit(text, (text_x, text_y))
            else:
                self.message = None

    def upgrade_click_amount(self):
        if self.player_square.score.score < self.cost:
            self.messanger.add_message("Not enough fragments!")
      
            return
        else:
            self.player_square.score.increase(-self.cost)
        self.player_square.click_amount += 1  # Increase the click amount by 1
        self.click_amount = self.player_square.click_amount #update the click amount
        self.cost += 50  # Increase the cost by 50
        print(f"Upgrade! Click amount is now {self.player_square.click_amount}, new cost is {self.cost}")