import pygame
import random

# Initialize the game
pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode((800, 600))

# Load the road runner image
road_runner = pygame.image.load("rayzr.jpg")

# Load the cactus image
cactus = pygame.image.load("soldier.jpg")

# Set the road runner starting position
road_runner_x = 50
road_runner_y = 500

# Set the cactus starting position
cactus_x = 800
cactus_y = 500

# Set the cactus movement speed
cactus_speed = 10

# Set the game clock
clock = pygame.time.Clock()

# Set the game loop flag
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Move the cactus to the left
    cactus_x -= cactus_speed
    
    # Check if the cactus has moved off the screen
    if cactus_x < -100:
        cactus_x = 800
        cactus_y = random.randint(0, 500)
    
    # Get the key events
    keys = pygame.key.get_pressed()
    
    # Move the road runner up or down based on the key events
    if keys[pygame.K_UP]:
        road_runner_y -= 5
    if keys[pygame.K_DOWN]:
        road_runner_y += 5
    
    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Draw the road runner and cactus on the screen
    screen.blit(road_runner, (road_runner_x, road_runner_y))
    screen.blit(cactus, (cactus_x, cactus_y))
    
    # Update the screen
    pygame.display.update()
    
    # Set the clock tick rate
    clock.tick(60)

# Quit the game
pygame.quit()
