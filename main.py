import pygame
import sys

# Initial setup
pygame.init()

# Constants
WIDTH, HEIGHT = 1080, 720
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player variables
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5
jumping = False
jump_count = 10
gravity = 5

# Platform variables
platform_width = 200
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - 50
# Platform variables
platform2_width = 200
platform2_height = 20
platform2_x = WIDTH // 6 - platform2_width // 6
platform2_y = HEIGHT - 50

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
    
    # Jumping
    if not jumping:
        if keys[pygame.K_w]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    player_x += (keys[pygame.K_d] - keys[pygame.K_a]) * player_speed

    # Keep the player within the screen boundaries
    player_x = max(0, min(WIDTH - player_size, player_x))

    # Check for collision with the platform
    if player_y + player_size >= platform_y and player_y <= platform_y + platform_height and \
            player_x + player_size >= platform_x and player_x <= platform_x + platform_width:
        if jumping and player_y + player_size < platform_y + 5:
            # Player is jumping and is above the platform, allow jumping on the platform
            player_y = platform_y - player_size
            jumping = False
            jump_count = 10
        elif not jumping:
            # Player is on the platform
            player_y = platform_y - player_size
            jump_count = 10
    if player_y + player_size >= platform2_y and player_y <= platform2_y + platform2_height and \
            player_x + player_size >= platform2_x and player_x <= platform2_x + platform2_width:
        if jumping and player_y + player_size < platform2_y + 5:
            # Player is jumping and is above the platform, allow jumping on the platform
            player_y = platform2_y - player_size
            jumping = False
            jump_count = 10
        elif not jumping:
            # Player is on the platform
            player_y = platform2_y - player_size
            jump_count = 10

    # Check for collision with the ground
    if player_y > HEIGHT:
        # Player touches the ground, reset the position
        player_x = WIDTH // 2 - player_size // 2
        player_y = HEIGHT - 2 * player_size

    # Gravity
    if player_y < HEIGHT - player_size and not jumping:
        player_y += gravity

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.rect(screen, BLUE, (platform2_x, platform2_y, platform2_width, platform2_height))
    pygame.display.flip()
    clock.tick(FPS)
