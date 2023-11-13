import pygame
import random
import time

pygame.init()

window_size = (800, 600)
pygame.display.set_caption('Graydon Metzler Flappy Bird')
screen = pygame.display.set_mode(window_size)

# Define circle properties
circle_radius = 25
circle_x = 100
circle_y = window_size[1] // 2
circle_speed = 5
circle_color = (0, 0, 255)

# Define variables for spawning a new circle
next_circle_time = time.time() + 1  # 1 second from now

# A Simple Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Spacebar pressed")

    # Move the circle to the right
    circle_x += circle_speed

    # Check if the circle hits the right screen boundary
    if circle_x + circle_radius >= window_size[0]:
        circle_x = 0  # Reset the circle's position to the left
        next_circle_time = time.time() + 1  # Schedule the next circle for 1 second from now

    screen.fill((255, 255, 255))  # Fill the screen with white color

    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))  # Draw a red rectangle

    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)  # Draw the moving circle

    pygame.display.flip()  # Update the display

    pygame.time.delay(30)

pygame.quit()