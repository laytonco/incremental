import pygame
from constants import *
from floatingtext import FloatingText
from size import SizeDisplay
from upgrades import UpgradeApp


class MainBlock:

    def __init__(self, x, y, width, height, size_display):
        self.click_amount = 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.original_width = width
        self.original_height = height
        self.size_display = size_display
        self.floating_texts = []
        self.clicked_within_block = False

    def draw(self, screen):
        pygame.draw.rect(screen, ("gray"), (self.x, self.y, self.width, self.height))
        self.floating_texts = [text for text in self.floating_texts if text.alpha > 0]
        for text in self.floating_texts:
            text.draw(screen)

    def click(self, x, y):
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            self.width = self.original_width * 0.8
            self.height = self.original_height * 0.8
            self.x += (self.original_width - self.width) / 2
            self.y += (self.original_height - self.height) / 2
            self.click_x = x
            self.click_y = y
            self.clicked_within_block = True
        else:
            self.clicked_within_block = False

    def release(self, click_amount):
        if self.clicked_within_block:
            self.x -= (self.original_width - self.width) / 2
            self.y -= (self.original_height - self.height) / 2
            self.width = self.original_width
            self.height = self.original_height
            self.floating_texts.append(FloatingText(self.click_x, self.click_y))
            self.size_display.update_size(self.size_display.current_size + click_amount)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            self.click(x, y)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.release(self.click_amount)

