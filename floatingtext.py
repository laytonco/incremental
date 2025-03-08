import pygame
from constants import *

class FloatingText:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alpha = 255
        
    
    def draw(self, screen):
        #will need to change this for upgrades
        current_score_rate = 1
        current_score_rate_text = "+" + str(current_score_rate)
        font = pygame.font.Font(None, 36)
        text = font.render(current_score_rate_text ,True, (255, 255, 255))
        text.set_alpha(self.alpha)
        screen.blit(text, (self.x, self.y))
        self.y -= 1
        self.alpha -= 2
