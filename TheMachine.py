# THE MACHINE =================================================================

# The purpose of this file is to display a visual machine that can mix and
# create chemicals to use to fulfill the customers' orders.

# Parent: main ================================================================
# Author: Liam Andrew Westlake =======================================================
# Editor: Nicholas Pribytkov ==================================================

# IMPORT PYTHON MODULES =======================================================
    
import pygame  # [LAW] main game functions
import random  # [LAW] This is used to randomize things
import pygame.freetype  # [LAW] This is used for the text on the screen
import os # [NP] This is used to obtain the parent (folder) file directory path for the game so we can access files within the folder itself

# START-UP ====================================================================

pygame.init() # [LAW] Initializes the Pygame
parentfile = os.path.dirname(__file__) # [NP] Find the path for the parent folder
pygame.init() # [LAW] Initialize Pygame
screen = pygame.display.set_mode((1300, 800)) # [LAW] Set the size of the screen
clock = pygame.time.Clock() # [LAW] Create a Pygame clock to control frame rates

Chemicals = ["H2O (Water)", "HCl (Hydrochloric Acid)", "NaOH (Sodium Hydroxide)", "NaCl (Sodium Chloride)", "NH3OH (Ammonia Hydroxide)", "NH4 (Ammonium)"]
orderchem = Chemicals[random.randint(0, len(Chemicals) - 1)]

# FLASK LOADER ================================================================

# [NP] Depending on the customer's desired chemical, the appropriate flask image file will be chosen.
if orderchem == "H2O (Water)":
    b = r"" + parentfile + "\Images\FlaskC.png"
elif orderchem == "NH3OH (Ammonia Hydroxide)" or orderchem == "NH4 (Ammonium)":
    b = r"" + parentfile + "\Images\Flask B.png"
else:
    b = r"" + parentfile + "\Images\Flask A.png"

Flask = pygame.image.load(b).convert_alpha() # [LAW] Load and convert the Flask image with alpha for transparency
FlaskB = Flask.copy() # [LAW] Make a copy of Flask for FlaskB

Flask = pygame.transform.scale(Flask, (200, 250)) # [LAW] Adjust the dimensions as needed
FlaskB = pygame.transform.scale(FlaskB, (200, 250)) # [LAW] Make FlaskB smaller

# MACHINE LOADER ==============================================================

background = pygame.image.load(r"" + parentfile + "\Images\Machine.png").convert_alpha() # [LAW] Load and convert the background image with alpha
background = pygame.transform.scale(background, (1300, 800)) # [LAW] Scale the background to fit the screen

# INITIALIZATION ==============================================================

# [LAW] Set the starting position of the Flask
position = Flask.get_rect()
position.topleft = (1000, 90)

running = True
Show_FlaskB = True
Move_Flask = False

# [LAW] Define the clickable area
click_area = pygame.Rect(700, 400, 50, 50)

# FLASK LOCOMOTIIVE CYCLE =====================================================

def MoveFlask():
    for x in range(100):
        screen.blit(background, (0, 0)) # [LAW] Ensure the background is drawn before everything else
        position.move_ip(3, 0) # [LAW] Move the Flask
        screen.blit(Flask, position) # [LAW] Draw the Flask in the new position
        pygame.display.update() # [LAW] Update the display
        clock.tick(10) # [LAW] Set the frame rate

# MAIN LOOP ===================================================================

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # [LAW] Allow the window to be closed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if click_area.collidepoint(mouse_pos): # [LAW] Check if the click is within the clickable area
                Show_FlaskB = False
                Move_Flask = True

    screen.blit(background, (0, 0)) # [LAW] Redraw the background

    if Show_FlaskB:
        screen.blit(FlaskB, (650, 90)) # [LAW] Display FlaskB at the new position

    if Move_Flask:
        position.move_ip(3, 0) # [LAW] Move the Flask
        screen.blit(Flask, position) # [LAW] Draw Flask in the new position

    # Optionally, draw the clickable area for debugging (you can comment this out later)
    # pygame.draw.rect(screen, (255, 0, 0), click_area, 2)

    pygame.display.update() # [LAW] Update the display
    clock.tick(10) # [LAW] Control the frame rate

# QUIT ========================================================================

pygame.quit() # [LAW] Quit Pygame after all the functions have been completed

# END =========================================================================




