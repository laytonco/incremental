import pygame
from constants import *

class MainBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.original_width = RECT_WIDTH
        self.original_height = RECT_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, ("gray"), (self.x, self.y, self.width, self.height))

    # click within rectangle 
    def click(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            self.width = self.original_width * 0.8
            self.height = self.original_height * 0.8
            self.x += (self.original_width - self.width) / 2
            self.y += (self.original_height - self.height) / 2
            print("Clicked!")

    def release(self):
        self.x -= (self.original_width - self.width) / 2
        self.y -= (self.original_height - self.height) / 2
        self.width = self.original_width
        self.height = self.original_height

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            self.click(x, y)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.release()