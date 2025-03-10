import pygame
import math
from helperfunctions import *
from playersquare import PlayerSquare
from score import Score
from constants import *
from upgradeclickamount import UpgradeClickAmount
from upgrademultiplier import UpgradeMultiplier
from autoclicker import Autoclicker
from projectile import Projectile
from message_manager import Messanger



# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Square Breaker")



#create text message
messanger = Messanger(None, 36)
# Create a score instance
score = Score(None, 36)

# Create a square instance
square = PlayerSquare(GRAY, 100, score)

# Define the initial click amount
click_amount = 1

# Create upgrade instances
upgrade_click_amount = UpgradeClickAmount(None, 36, square, messanger, click_amount)
upgrade_multiplier = UpgradeMultiplier(None, 36, square, upgrade_click_amount.button_rect.bottom + 10, messanger, click_amount)
autoclicker = Autoclicker(None, 36, square, upgrade_multiplier.button_rect.bottom + 10, messanger)

# tick rate:
tick_rate = 60
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            square.click(x, y)
            upgrade_click_amount.click(x, y)
            upgrade_multiplier.click(x, y)
            autoclicker.click(x, y)

    # Fill the background
    screen.fill(BLACK)

    # Draw the square
    square.draw(screen)

    # Draw the score
    score.draw(screen)

    # Draw the upgrade buttons and costs
    upgrade_click_amount.draw(screen)
    upgrade_multiplier.draw(screen)
    autoclicker.draw(screen)

    #draw messages
    messanger.draw(screen)

    # Draw the projectiles
    for projectile in autoclicker.projectiles[:]:
        projectile.move()
        projectile.draw(screen)
        if pygame.Rect.colliderect(projectile.rect, square.rect):
            autoclicker.projectiles.remove(projectile)
            square.click()

        if projectile.rect.bottom < 0:
            autoclicker.projectiles.remove(projectile)

    # Check if autoclicker is enabled and click the square
    autoclicker.autoclick()
    if autoclicker.enabled:
        autoclicker.autoclicker_sprite(screen)
        autoclicker.update(pygame.time.get_ticks(), screen)

    # Update the display
    pygame.display.flip()
    clock.tick(tick_rate)

# Quit Pygame
pygame.quit()