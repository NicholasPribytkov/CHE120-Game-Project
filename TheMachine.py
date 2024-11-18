# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:25:09 2024

@author: liama
"""

import pygame  # LAW main game functions
import random  # This is used to randomize things
import pygame.freetype  # This is used for the text on the screen

# Initialize Pygame
pygame.init()

Chemicals = ["H2O (Water)", "HCl (Hydrochloric Acid)", "NaOH (Sodium Hydroxide)", "NaCl (Sodium Chloride)", "NH3OH (Ammonia Hydroxide)", "NH4 (Ammonium)"]
orderchem = Chemicals[random.randint(0, len(Chemicals) - 1)]

screen = pygame.display.set_mode((1300, 800))  # Set the size of the screen
clock = pygame.time.Clock()  # Create a Pygame clock to control frame rates

if orderchem == "H2O (Water)":
    b = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\FlaskC.png"
elif orderchem == "NH3OH (Ammonia Hydroxide)" or orderchem == "NH4 (Ammonium)":
    b = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Flask B.png"
else:
    b = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Flask A.png"

Flask = pygame.image.load(b).convert_alpha()  # Load and convert the Flask image with alpha for transparency
FlaskB = Flask.copy()  # Make a copy of Flask for FlaskB

# Resize Flask and FlaskB images
Flask = pygame.transform.scale(Flask, (200, 250))  # Adjust the dimensions as needed
FlaskB = pygame.transform.scale(FlaskB, (200, 250))  # Make FlaskB smaller

background = pygame.image.load(r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Machine.png").convert_alpha()  # Load and convert the background image with alpha
background = pygame.transform.scale(background, (1300, 800))  # Scale the background to fit the screen

# Set the starting position of the Flask
position = Flask.get_rect()
position.topleft = (1000, 90)  # Set the starting position

running = True
Show_FlaskB = True
Move_Flask = False

# Define the clickable area
click_area = pygame.Rect(700, 400, 50, 50)

def MoveFlask():
    for x in range(100):
        screen.blit(background, (0, 0))  # Ensure the background is drawn before everything else
        position.move_ip(3, 0)  # Move the Flask
        screen.blit(Flask, position)  # Draw the Flask in the new position
        pygame.display.update()  # Update the display
        clock.tick(10)  # Set the frame rate

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Allow the window to be closed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if click_area.collidepoint(mouse_pos):  # Check if the click is within the clickable area
                Show_FlaskB = False
                Move_Flask = True

    screen.blit(background, (0, 0))  # Redraw the background

    if Show_FlaskB:
        screen.blit(FlaskB, (650, 90))  # Display FlaskB at the new position

    if Move_Flask:
        position.move_ip(3, 0)  # Move the Flask
        screen.blit(Flask, position)  # Draw Flask in the new position

    # Optionally, draw the clickable area for debugging (you can comment this out later)
    # pygame.draw.rect(screen, (255, 0, 0), click_area, 2)

    pygame.display.update()  # Update the display
    clock.tick(10)  # Control the frame rate

pygame.quit()  # Quit Pygame after all the functions have been completed




