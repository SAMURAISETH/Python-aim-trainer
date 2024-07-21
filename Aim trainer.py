import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Training Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Target settings
target_radius = 20
target_color = red
target_pos = (random.randint(target_radius, width - target_radius),
              random.randint(target_radius, height - target_radius))

# Aim bot settings
aimbot_active = True
aimbot_speed = 5  # pixels per frame

# Hit marker settings
hit_marker_color = white
hit_marker_radius = 30
hit_marker_show_time = 500  # milliseconds

# Game variables
score = 0
hit_marker_visible = False
hit_marker_time = 0

# Font settings
font = pygame.font.Font(None, 36)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Move the aimbot towards the target if aimbot is active
    if aimbot_active:
        angle = math.atan2(target_pos[1] - mouse_y, target_pos[0] - mouse_x)
        mouse_x += int(aimbot_speed * math.cos(angle))
        mouse_y += int(aimbot_speed * math.sin(angle))
        pygame.mouse.set_pos(mouse_x, mouse_y)

    # Check for collision with the target
    distance = math.hypot(mouse_x - target_pos[0], mouse_y - target_pos[1])
    if distance <= target_radius:
        score += 1
        hit_marker_visible = True
        hit_marker_time = pygame.time.get_ticks()
        target_pos = (random.randint(target_radius, width - target_radius),
                      random.randint(target_radius, height - target_radius))

    # Clear screen
    window.fill(black)

    # Draw the target
    pygame.draw.circle(window, target_color, target_pos, target_radius)

    # Draw the hit marker if visible
    if hit_marker_visible:
        pygame.draw.circle(window, hit_marker_color, target_pos, hit_marker_radius)
        if pygame.time.get_ticks() - hit_marker_time > hit_marker_show_time:
            hit_marker_visible = False

    # Draw the score
    score_text = font.render(f"Score: {score}", True, white)
    window.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
