# WORKING MOVING GOOSE ========================================================

# Parent: main ================================================================
# Author: Liam Westlake =======================================================
# Editor(s): Nicholas Pribytkov ===============================================

# IMPORT PYTHON MODULES =======================================================

import pygame  # [LAW] main game functions
import random  # [LAW] This is used to randomize things
import pygame.freetype  # [LAW] This is used for the text on the screen
import time  # [LAW] used for text showing up after a certain time has passed
import os # [NP] This is used to obtain the parent (folder) file directory path for the game so we can access files within the folder itself

# IMPORT PY FILES =============================================================

from CustomerOrders import CustomerOrder # [NP] This file helps the customers formulte their order

# START-UP ======================================================================

pygame.init() # [LAW] Initializes the Pygame
parentfile = os.path.dirname(__file__) # [NP] Find the path for the parent folder

# ASSET CALL ==================================================================

# [LAW] Define file paths of the geese
# [NP] Use the parent folder's path and add a suffix to build the paths of the geese (this is so it works on all computers regardless of directory)

HAM = r"" + parentfile + "\Images\Goose4.png"
MAT = r"" + parentfile + "\Images\Goose5.png"
PEND = r"" + parentfile + "\Images\Goose6.png"
NICK = r"" + parentfile + "\Images\Goose7.png"
ZINO = r"" + parentfile + "\Images\Goose8 (1).png"
HELMET = r"" + parentfile + "\Images\Goose8.png"
KATIE = r"" + parentfile + "\Images\Goose9.png"
LAW = r"" + parentfile + "\Images\Goose1.png"
GLIAM = r"" + parentfile + "\Images\Goose2.png"
KAMKAR = r"" + parentfile + "\Images\Goose3.png"
Speech = r"" + parentfile + "\Images\Speech-Bubble.png"
Background = r"" + parentfile + "\Images\R.png"
MachineIMG= r"" + parentfile + "\Images\Machine.png"

Pics = [HAM, MAT, PEND, NICK, ZINO, HELMET, KATIE, LAW, GLIAM, KAMKAR] # [LAW] List of geese

# CUSTOMER ORDERS =============================================================

GooseImage = random.choice(Pics) # [LAW] Selects a random goose
Greeting = ['Hello', 'Hows it going', 'Hi'] # [LAW] List of greetings

Order = CustomerOrder() # [NP] Call the Customer Order function, which returns a list containing [Quantity, Unit, Chemical]

OrderA = random.choice(Greeting)+ " " + "I Need " + Order[0] # [LAW] Order with random greeting and a random chemical
OrderB = Order[1] + " " + Order[2]
screen = pygame.display.set_mode((1300, 800)) # [LAW] Sets the size of the screen
clock = pygame.time.Clock() # [LAW] Creates a Pygame clock to control frame rates

player = pygame.image.load(GooseImage).convert_alpha() # [LAW] Loads and converts the goose image
background = pygame.image.load(Background).convert_alpha() # [LAW] Loads and converts the background image
speech_bubble = pygame.image.load(Speech).convert_alpha() # [LAW] Loads and converts the speech bubble image
speech_bubble= pygame.transform.scale(speech_bubble, (550,550)) # [LAW] Resizes the speech bubble

Machine = pygame.image.load(MachineIMG).convert()
Machine = pygame.transform.scale(Machine, (1300, 800))  # [LAW] Scale the second Background to fit

position = player.get_rect() # [LAW] Gets the position of the player

BLACK = (0, 0, 0) # [LAW] Defines colors

font = pygame.freetype.SysFont("Calibri", 40) # [LAW] Sets the font and size of the text

click_area = pygame.Rect(700, 400, 50, 50)# [LAW] Defines the clickable area for the mouse interactions with buttons
click_area2 = pygame.Rect(700, 50, 50, 50)

# DISPLAY LOOP ================================================================

for x in range(100): # [LAW] This tells the following the repeat 100 times
    screen.blit(background, (0, 0)) # [LAW] Ensures background is drawn before everything else
    position = position.move(1.5, 0) # [LAW] Moves the player
    screen.blit(player, position) # [LAW] Draws the player in the new position
    pygame.display.update() # [LAW] Updates the display
    clock.tick(30) # [LAW] Sets the frame rate

# ORDER TEXT FUNCTION =========================================================

def display_text(text, x, y):
    font.render_to(screen, (x, y), text, BLACK)

# BUTTON SIZING ===============================================================

button_rect = pygame.Rect(1000, 750, 250, 60)  # [LAW] Position the first button
button_rect2 = pygame.Rect(1000, 650, 250, 60)  # [LAW] Position the second button

# INITIALIZATION ==============================================================

# [LAW] Initializes timer and control variables
start_time = time.time()
show_text = False
show_speech_bubble = False
show_goose = True
show_background = True
show_machine = False
show_things = False
running = True


# MAIN TEXT LOOP ==============================================================

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # [LAW] Allows the window to be closed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos): # [LAW] Checks if click is on the first button
                show_things = True
            elif button_rect2.collidepoint(mouse_pos): # [LAW] Checks if click is on the second button
                running = False

    # [LAW] Checks if 1.25 seconds have elapsed
    if not show_text and time.time() - start_time >= 1.25:
        show_text = True
        show_speech_bubble = True

    # [LAW] This goes to the machine after the player clicks the first button
    if show_things: 
        show_text = False
        show_speech_bubble = False
        show_machine = True

    screen.blit(background, (0, 0)) # [LAW] Redraws the background
    screen.blit(player, position) # [LAW] Redraws the player at the current position

    # [LAW] Displays text and speech bubble after two seconds have passed
    if show_speech_bubble:
        screen.blit(speech_bubble, (700, 10)) # [LAW] Position the speech bubble
        display_text(OrderA, 760, 150) # [LAW] Adjusts text position to fit inside the speech bubble
        display_text(OrderB, 760, 190)
        
    # [LAW] Draw the first button
    pygame.draw.rect(screen, (0, 0, 225), button_rect)  # Blue button
    font = pygame.freetype.SysFont(None, 36)
    font.render_to(screen, (1010, 760), "Accept Order", (225, 255, 255))  # White text

    # [LAW]  Draw the second button
    pygame.draw.rect(screen, (225, 0, 0), button_rect2)  # Red button
    font.render_to(screen, (1010, 660), "Reject Order", (225, 255, 255))  # White text

    # [LAW] Renders the machine ontop of the old background
    if show_machine:
        screen.blit(Machine, (0, 0))

    # [LAW] Updates the display with this text
    pygame.display.update()
    clock.tick(10) # [LAW] Control the frame rate

# QUIT ========================================================================

pygame.quit() # [LAW] Quits Pygame after all the functions have been completed

# END =========================================================================
    
