# WORKING MOVING GOOSE ========================================================

# This file displays the visuals of the customer ordering sequence.

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

# [KY] import functions
from CustomerOrders import CustomerOrder # [NP] This file helps the customers formulte their order
from Order_Match import order_match # [KY] This function returns points per order
from Order_Match import accuracy_as_percent # [KY] This function returns amount accuracy as a percent by comparing the quantities of chem ordered and chem produced, to be used in fail system)

# ASSET CALL ==================================================================

parentfile = os.path.dirname(__file__) # [NP] Find the path for the parent folder

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

#Instructions for each order
NaClin = '''You are making Sodium Chloride:
            - Step 1
            - Step 2
            - Step 3
            - Step 4'''
NH3in = '''You are making Ammonia:
            - Step 1
            - Step 2
            - Step 3
            - Step 4'''
NH4OHin = '''You are making Ammonium Hydroxide:
            - Step 1
            - Step 2
            - Step 3
            - Step 4'''
HClin = '''You are making Hydrochloric Acid:
            - Step 1
            - Step 2
            - Step 3
            - Step 4'''
NaOHin = '''You are making Sodium Hydroxide:
            - Step 1
            - Step 2
            - Step 3
            - Step 4'''
instruction_list=[NaClin,NH3in,NH4OHin,HClin,NaOHin]

# SET-UP ======================================================================

pygame.init()

screen = pygame.display.set_mode((1300, 800)) # [LAW] Sets the size of the screen
clock = pygame.time.Clock() # [LAW] Creates a Pygame clock to control frame rates

background = pygame.image.load(Background).convert_alpha() # [LAW] Loads and converts the background image
speech_bubble = pygame.image.load(Speech).convert_alpha() # [LAW] Loads and converts the speech bubble image
speech_bubble= pygame.transform.scale(speech_bubble, (550,550)) # [LAW] Resizes the speech bubble
 
Machine = pygame.image.load(MachineIMG).convert()
Machine = pygame.transform.scale(Machine, (1300, 800))  # [LAW] Scale the second Background to fit

BLACK = (0, 0, 0) # [LAW] Defines colors
 
font = pygame.freetype.SysFont("Calibri", 40) # [LAW] Sets the font and size of the text
font2 = pygame.freetype.SysFont("Calibri",25)

click_area = pygame.Rect(700, 400, 50, 50) # [LAW] Defines the clickable area for the mouse interactions with buttons
click_area2 = pygame.Rect(700, 50, 50, 50)
click_area3 = click_area = pygame.Rect(700, 400, 50, 50)

button_rect = pygame.Rect(1000, 750, 250, 60)  # [LAW] Position the first button
button_rect2 = pygame.Rect(1000, 650, 250, 60)  # [LAW] Position the second button


global player
global position

global OrderA
global OrderB

# CUSTOMER ORDERS =============================================================

def Customer():
    
    GooseImage = random.choice(Pics) # [LAW] Selects a random goose
    Greeting = ['Hello', 'Hows it going', 'Hi'] # [LAW] List of greetings
    
    Order = CustomerOrder() # [NP] Call the Customer Order function, which returns an object with quantity as a property
    
    OrderA = random.choice(Greeting)+ " " + "I Need " + Order # [LAW] Order with random greeting and a random chemical
    OrderB = "mol " + Order.Quantity
    
    player = pygame.image.load(GooseImage).convert_alpha() # [LAW] Loads and converts the goose image   
    position = player.get_rect() # [LAW] Gets the position of the player

if orderchem == "H2O (Water)":
    b = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\FlaskC.png"
elif orderchem == "NH3OH (Ammonia Hydroxide)" or orderchem == "NH4 (Ammonium)":
    b = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Flask B.png"
else:
    b = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Flask A.png"

# SET UP THE FLASKS ============================================================
Flask = pygame.image.load(b).convert_alpha()  # [LAW] Load and convert the Flask image with alpha for transparency
FlaskB = Flask.copy()  # [LAW] Make a copy of Flask for FlaskB

# [LAW] Resize Flask and FlaskB images
Flask = pygame.transform.scale(Flask, (200, 250))  # [LAW] Adjust the dimensions as needed
FlaskB = pygame.transform.scale(FlaskB, (200, 250))  # [LAW] Make FlaskB smaller

# [LAW] Set the starting position of the moving Flask
flask_position= Flask.get_rect()
flask_position.topleft = (1000, 90)  

# DISPLAY LOOP ================================================================

    for x in range(100): # [LAW] This tells the following the repeat 100 times
        screen.blit(background, (0, 0)) # [LAW] Ensures background is drawn before everything else
        position = position.move(1.5, 0) # [LAW] Moves the player
        screen.blit(player, position) # [LAW] Draws the player in the new position
        pygame.display.update() # [LAW] Updates the display
        clock.tick(30) # [LAW] Sets the frame rate
        
    return player, position, OrderA, OrderB, Order, Order.Quantity
        
# ORDER TEXT FUNCTION =========================================================

def display_text(text, x, y):
    font.render_to(screen, (x, y), text, BLACK)

# INSTRUCTION TEXT ===========================================================
def display_text2(text, x, y):
    lines = text.split('\n')# [LAW] This allows there to be a list of instructions
    for i, line in enumerate(lines):
        font2.render_to(screen, (x, y + i * 30), line.strip(), BLACK)

for i in range(len(Chemicals)): # [LAW] Finds what Chemical has been ordered and asigns the instructions to the instructions variable
    if Chemicals[i] in orderchem:
        instructions= instruction_list[i]
# MOVING THE FLASK ============================================================
def MoveFlask():
    for x in range(100):
        screen.blit(background, (0, 0))  # Ensure the background is drawn before everything else
        position.move_ip(3, 0)  # Move the Flask
        screen.blit(Flask, flask_position)  # Draw the Flask in the new position
        pygame.display.update()  # Update the display
        clock.tick(10)  # Set the frame rate
# INITIALIZATION ==============================================================
    
# MAIN TEXT LOOP ==============================================================

def Runtime(player, position, OrderA, OrderB, show, Order1, Order2):
    
    running = True
    
    # [LAW] Initializes timer and control variables
    start_time = time.time()
    show_speech_bubble = show
    show_goose = True
    show_background = True
    show_machine = False
    show_things = False
    show_text = show
    Show_FlaskB = False
    Move_Flask = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # [LAW] Allows the window to be closed
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos): # [LAW] Checks if click is on the first button
                    show_things = True
                    Show_FlaskB = True
                elif button_rect2.collidepoint(mouse_pos): # [LAW] Checks if click is on the second button
                    running = False
                    pygame.quit() # [LAW] Allows the window to be closed
                elif click_area3.collidepoint(mouse_pos): # [KY] Checks if done button is pressed
                    Move_Flask = True
                    Show_FlaskB = False

                    # [KY] - call order match and accuracy as percent functions 
                    order_points = order_match(output, orderchem) 
                    order_accuracy = accuracy_as_percent(output, orderchem)    

        # [LAW] Checks if 1.25 seconds have elapsed
        if not show_text and time.time() - start_time >= 1.25:
            show_text = True
            show_speech_bubble = True
    
        # [LAW] This goes to the machine after the player clicks the first button
        if show_things: 
            show_text = False
            show_speech_bubble = False
            show_machine = True
            show_instructions=True
            return [Order1, Order2]
    
        screen.blit(background, (0, 0)) # [LAW] Redraws the background
        screen.blit(player, position) # [LAW] Redraws the player at the current position
    
        # [LAW] Displays text and speech bubble after two seconds have passed
        if show_speech_bubble:
            screen.blit(speech_bubble, (700, 10)) # [LAW] Position the speech bubble
            display_text(OrderA, 760, 150) # [LAW] Adjusts text position to fit inside the speech bubble
            display_text(OrderB, 760, 190) 
            
        # [LAW] Draw the first button
        pygame.draw.rect(screen, (0, 0, 225), button_rect)  # [LAW] Blue button
        font = pygame.freetype.SysFont(None, 36)
        font.render_to(screen, (1010, 760), "Accept Order", (225, 255, 255))  # [LAW] White text
    
        # [LAW]  Draw the second button
        pygame.draw.rect(screen, (225, 0, 0), button_rect2)  # [LAW] Red button
        font.render_to(screen, (1010, 660), "QUIT", (225, 255, 255))  # [LAW] White text

        if show_machine: # [LAW] Makes the machine the new background
           screen.blit(Machine, (0, 0))
    
        if show_instructions: # [LAW] Displays the instructions
           display_text2(instructions, 30, 250)
    
        if Show_FlaskB:
           screen.blit(FlaskB, (650, 90))  # [LAW] Display FlaskB at the new position
        
        if Move_Flask:
           position.move_ip(3, 0)  # [LAW] Move the Flask
           screen.blit(Flask, position)  # [LAW] Draw Flask in the new position

        # [LAW] Updates the display with this text
        pygame.display.update()
        clock.tick(10) # [LAW] Control the frame rate

# END =========================================================================
    
