import pygame
import math
from constants import *
from helperfunctions import *
from projectile import Projectile

class Autoclicker:
    def __init__(self, font, size, player_square, y_offset, messanger, projectiles):
        self.messanger = messanger
        self.num_circles = 0
        self.projectiles = projectiles  # Use the projectiles list from main.py
        self.font = pygame.font.Font(font, size)
        self.radius = 250 # distance from the center of the square
        self.angle = 0
        self.cost = 100
        self.text = "Autoclicker"
        self.player_square = player_square  # Reference to the player square
        self.enabled = False  # Autoclicker initially disabled
        self.last_click_time = 0  # Time of the last autoclick
        self.click_interval = 1000  # Interval between autoclicks in milliseconds
        self.button_rect = pygame.Rect(10, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.rotation_speed = 0.5 # Speed of the rotation

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

        # Render the number of circles
        if self.num_circles > 0:
            circles_text = self.font.render(f"Circles: {self.num_circles}", True, (255, 255, 255))
            circles_rect = circles_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top + 25))
            surface.blit(circles_text, circles_rect)

    def click(self, x, y):
        if self.button_rect.collidepoint(x, y):
            self.enable_autoclicker()

    def enable_autoclicker(self):
        if self.player_square.score.score < self.cost:
            self.messanger.add_message("Not enough fragments!")
            return
        else:
            self.player_square.score.increase(-self.cost)
            self.num_circles += 1
            self.cost = int(self.cost * 1.25)  # Increase the cost exponentially
            
        self.enabled = True  # Enable the autoclicker
        self.last_click_time = pygame.time.get_ticks()  # Initialize the last click time

        print("Autoclicker enabled!")

    def autoclick(self):
        current_time = pygame.time.get_ticks()
        if self.enabled and current_time - self.last_click_time >= self.click_interval:
            self.last_click_time = current_time
            
            # Get center of the square
            center_x = self.player_square.rect.centerx
            center_y = self.player_square.rect.centery

            for i in range(self.num_circles):
                # Calculate the angle for this circle (evenly distributed)
                circle_angle = self.angle + (360 / self.num_circles) * i
                # Convert angle to radians
                angle_rad = math.radians(circle_angle)

                # Spawn projectiles
                projectile_x = self.player_square.rect.centerx + int(self.radius * math.cos(angle_rad))
                projectile_y = self.player_square.rect.centery + int(self.radius * math.sin(angle_rad))
            
                # Target coordinates
                target_x = self.player_square.rect.centerx
                target_y = self.player_square.rect.centery

                self.projectiles.append(Projectile(int(projectile_x), int(projectile_y), target_x, target_y))

    def autoclicker_sprite(self, surface):
        self.angle += self.rotation_speed  # Increase this for faster rotation

        # Keep the angle within 0-360 degrees
        if self.angle >= 360:
            self.angle -= 360

        # Convert degrees to radians
        radians = math.radians(self.angle)

        # Calculate new position based on angle and radius
        circle_x = self.player_square.rect.centerx + int(self.radius * math.cos(radians))
        circle_y = self.player_square.rect.centery + int(self.radius * math.sin(radians))

        # Draw the sprite
        pygame.draw.circle(surface, (255, 255, 255), (circle_x, circle_y), 20)

    def update(self, current_time, surface):
        if not self.enabled:
            return
        
        # Only draw circles if we have at least one
        if self.num_circles > 0:
            # Update the position of each circle
            self.angle += self.rotation_speed
            if self.angle >= 360:
                self.angle = 0
                
            # Get the center of the player square
            center_x = self.player_square.rect.centerx
            center_y = self.player_square.rect.centery
            
            # Draw each circle at a different angle
            for i in range(self.num_circles):
                # Calculate the angle for this circle (evenly distributed)
                circle_angle = self.angle + (360 / self.num_circles) * i
                # Convert angle to radians
                angle_rad = math.radians(circle_angle)
                # Calculate position
                x = center_x + self.radius * math.cos(angle_rad)
                y = center_y + self.radius * math.sin(angle_rad)
                # Draw the circle
                pygame.draw.circle(surface, (255, 255, 255), (int(x), int(y)), 20)



