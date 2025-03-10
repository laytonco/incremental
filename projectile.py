import pygame
import math
from constants import *
from helperfunctions import *


class Projectile:
    def __init__(self, x, y, target_x, target_y, speed=5):
        self.rect = pygame.Rect(x, y, 10, 5)  # Small square projectile
        self.speed = speed  # Movement speed

        # Calculate direction vector
        direction_x = target_x - x
        direction_y = target_y - y
        length = math.sqrt(direction_x ** 2 + direction_y ** 2)  # Distance to target

        # Normalize to get unit vector
        if length != 0:
            self.velocity_x = (direction_x / length) * speed
            self.velocity_y = (direction_y / length) * speed
        else:
            self.velocity_x, self.velocity_y = 0, 0  # Prevent division by zero

    def move(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)  # Draw white projectile