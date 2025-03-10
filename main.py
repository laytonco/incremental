import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Square Breaker")

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Define a common button size
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

# Define the square object
class PlayerSquare:
    def __init__(self, color, size, score):
        self.color = color
        self.size = size
        self.rect = pygame.Rect((1280 - size) // 2, (700 - size) // 2, size, size)
        self.score = score
        self.click_amount = 1  # Initial click amount

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def click(self, x=None, y=None):
        if x is None and y is None or self.rect.collidepoint(x, y):
            self.score.increase(self.click_amount)

########## SCORE CLASS ##########
class Score:
    def __init__(self, font, size):
        self.score = 0
        self.font = pygame.font.Font(font, size)

    def increase(self, amount=1):
        self.score += amount

    def draw(self, surface):
        score_text = self.font.render(f"Fragments: {self.score:.2f}", True, GRAY)
        surface.blit(score_text, (screen.get_width() - score_text.get_width() - 10, 10))

class UpgradeClickAmount:
    def __init__(self, font, size, player_square):
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
        cost_text = self.font.render(f"Cost: {self.cost}", True, (255, 255, 255))
        cost_rect = cost_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top))
        surface.blit(cost_text, cost_rect)

    def click(self, x, y):
        if self.button_rect.collidepoint(x, y):
            self.upgrade_click_amount()

    def upgrade_click_amount(self):
        if self.player_square.score.score < self.cost:
            print("Not enough fragments!")
            return
        else:
            self.player_square.score.increase(-self.cost)
        self.player_square.click_amount += 1  # Increase the click amount by 1
        self.cost += 50  # Increase the cost by 50
        print(f"Upgrade! Click amount is now {self.player_square.click_amount}, new cost is {self.cost}")

class UpgradeSize:
    def __init__(self, font, size, player_square, y_offset):
        self.font = pygame.font.Font(font, size)
        self.cost = 50
        self.text = "Size 1.5x"
        self.player_square = player_square  # Reference to the player square
        self.button_rect = pygame.Rect(10, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

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
        cost_text = self.font.render(f"Cost: {self.cost}", True, (255, 255, 255))
        cost_rect = cost_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top))
        surface.blit(cost_text, cost_rect)

    def click(self, x, y):
        if self.button_rect.collidepoint(x, y):
            self.upgrade_size()

    def upgrade_size(self):
        if self.player_square.score.score < self.cost:
            print("Not enough fragments!")
            return
        else:
            self.player_square.score.increase(-self.cost)
        self.player_square.size += 1  # Increase the size by 1
        self.player_square.click_amount *= 1.5  # Increase the click amount by 1.5x
        self.player_square.rect = pygame.Rect((1280 - self.player_square.size) // 2, (700 - self.player_square.size) // 2, self.player_square.size, self.player_square.size)
        self.cost += 50  # Increase the cost by 50
        print(f"Upgrade! Size is now {self.player_square.size}, new cost is {self.cost}")

class Autoclicker:
    def __init__(self, font, size, player_square, y_offset):
        self.projectiles = []
        self.font = pygame.font.Font(font, size)
        self.radius = 250 # distance from the center of the square
        self.angle = 0
        self.cost = 1000
        self.text = "Autoclicker"
        self.player_square = player_square  # Reference to the player square
        self.enabled = False  # Autoclicker initially disabled
        self.last_click_time = 0  # Time of the last autoclick
        self.click_interval = 1000  # Interval between autoclicks in milliseconds
        self.button_rect = pygame.Rect(10, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

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
        cost_text = self.font.render(f"Cost: {self.cost}", True, (255, 255, 255))
        cost_rect = cost_text.get_rect(topleft=(self.button_rect.right + 5, self.button_rect.top))
        surface.blit(cost_text, cost_rect)

    def click(self, x, y):
        if self.button_rect.collidepoint(x, y):
            self.enable_autoclicker()

    def enable_autoclicker(self):
        if self.player_square.score.score < self.cost:
            print("Not enough fragments!")
            return
        else:
            self.player_square.score.increase(-self.cost)
            
        self.enabled = True  # Enable the autoclicker
        self.last_click_time = pygame.time.get_ticks()  # Initialize the last click time

        print("Autoclicker enabled!")

    def autoclick(self):
        current_time = pygame.time.get_ticks()
        if self.enabled and current_time - self.last_click_time >= self.click_interval:
            self.player_square.click()
            self.last_click_time = current_time

            #spawn projectiles
            projectile_x = self.player_square.rect.centerx +self.radius * math.cos(self.angle)
            projectile_y = self.player_square.rect.centery +self.radius * math.sin(self.angle)

            #target coordinates
            target_x = self.player_square.rect.centerx
            target_y = self.player_square.rect.centery

            self.projectiles.append(Projectile(int(projectile_x), int(projectile_y), target_x, target_y))

    def autoclicker_sprite(self):
        self.angle += 0.05

        circle_x = self.player_square.rect.centerx + self.radius * math.cos(self.angle)
        circle_y = self.player_square.rect.centery + self.radius * math.sin(self.angle)

        sprite_color = ("White")
        pygame.draw.circle(screen, sprite_color, (circle_x, circle_y), 20)


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


    
# Create a score instance
score = Score(None, 36)

# Create a square instance
square = PlayerSquare(GRAY, 100, score)

# Create upgrade instances
upgrade_click_amount = UpgradeClickAmount(None, 36, square)
upgrade_size = UpgradeSize(None, 36, square, upgrade_click_amount.button_rect.bottom + 10)
autoclicker = Autoclicker(None, 36, square, upgrade_size.button_rect.bottom + 10)

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
            upgrade_size.click(x, y)
            autoclicker.click(x, y)

    # Fill the background
    screen.fill(BLACK)

    # Draw the square
    square.draw(screen)

    # Draw the score
    score.draw(screen)

    # Draw the upgrade buttons and costs
    upgrade_click_amount.draw(screen)
    upgrade_size.draw(screen)
    autoclicker.draw(screen)

    # Draw the projectiles
    for projectile in autoclicker.projectiles[:]:
        projectile.move()
        projectile.draw(screen)
        if pygame.Rect.colliderect(projectile.rect, square.rect):
            autoclicker.projectiles.remove(projectile)

        if projectile.rect.bottom < 0:
            autoclicker.projectiles.remove(projectile)

    # Check if autoclicker is enabled and click the square
    autoclicker.autoclick()
    if autoclicker.enabled:
        autoclicker.autoclicker_sprite()

    # Update the display
    pygame.display.flip()
    clock.tick(tick_rate)

# Quit Pygame
pygame.quit()