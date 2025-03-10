import pygame
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Square Breaker")

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Define the square object
class PlayerSquare:
    def __init__(self, color, size, score):
        self.color = color
        self.size = size
        self.rect = pygame.Rect((1280 - size) // 2, (700 - size) // 2, size, size)
        self.score = score

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            self.score.increase(1)
            print("Square clicked!")

class Score:
    def __init__(self, font, size):
        self.score = 0
        self.font = pygame.font.Font(font, size)

    def increase(self, amount=1):
        self.score += amount

    def draw(self, surface):
        score_text = self.font.render(f"Fragments: {self.score}", True, GRAY)
        surface.blit(score_text, (screen.get_width() - score_text.get_width() - 10, 10))

# Create a score instance
score = Score(None, 36)

# Create a square instance
square = PlayerSquare(GRAY, 100, score)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            square.click(x, y)

    # Fill the background
    screen.fill(BLACK)

    # Draw the square
    square.draw(screen)

    # Draw the score
    score.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()