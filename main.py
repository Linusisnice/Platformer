import pygame
import sys

# Initial setup
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player variables
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Platform variables
platform_width = 200
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - 50

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Keep the player within the screen boundaries
    player_x = max(0, min(WIDTH - player_size, player_x))

    # Check for collision with the platform
    if player_y + player_size > platform_y and player_x < platform_x + platform_width and player_x + player_size > platform_x:
        player_y = platform_y - player_size

    # Gravity
    if player_y < HEIGHT - player_size:
        player_y += 5

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))

    pygame.display.flip()
    clock.tick(FPS)