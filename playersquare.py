import pygame
import math
import sys
from floatingtext import FloatingText

# Define the square object
class PlayerSquare:
    def __init__(self, color, size, score):
        self.color = color
        self.size = size
        self.rect = pygame.Rect((1280 - size) // 2, (700 - size) // 2, size, size)
        self.score = score
        self.click_amount = 1  # Initial click amount
        self.floating_texts = []
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.floating_texts = [text for text in self.floating_texts if text.draw(surface)]

    def click(self, x=None, y=None):
        if x is None and y is None or self.rect.collidepoint(x, y):
            self.score.increase(self.click_amount)
            if x is not None and y is not None:
                self.floating_texts.append(FloatingText(self.click_amount, (x, y), self.font))

    def hit_by_projectile(self, x, y):
        self.score.increase(self.click_amount)
        self.floating_texts.append(FloatingText(self.click_amount, (x, y), self.font))
    def update_cracks(self):
        # Define thresholds for cracks
        thresholds = [10000, 100000, 30000, 50000]  # Example thresholds for cracks
        crack_images = [
            pygame.image.load('crack1.png'),
            pygame.image.load('crack2.png'),
            pygame.image.load('crack3.png'),
            pygame.image.load('crack4.png')
        ]

        # Determine which crack image to display based on score
        for i, threshold in enumerate(thresholds):
            if self.score.value >= threshold:
                self.crack_image = crack_images[i]
            else:
                break

        # If score exceeds the last threshold, the square falls apart
        if self.score.value >= thresholds[-1]:
            self.fall_apart()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if hasattr(self, 'crack_image'):
            surface.blit(self.crack_image, self.rect.topleft)
        self.floating_texts = [text for text in self.floating_texts if text.draw(surface)]

    def fall_apart(self):
        # Logic to make the square fall apart
        print("The square has fallen apart!")
        # You can add more complex logic here, such as animations or removing the square