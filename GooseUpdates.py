# GOOSE UPDATES ===============================================================

# This file acts as the backbone of the game. It's main purpose is to update
# the UI and both calls and runs game mechanic files.

# Author: Liam Westlake =======================================================
# Editor(s): Nicholas Pribytkov, Katie Yu =====================================

# IMPORT PYTHON MODULES =======================================================

import pygame  # [LAW] main game functions
import random  # [LAW] This is used to randomize things
import pygame.freetype  # [LAW] This is used for the text on the screen
import time  # [LAW] used for text showing up after a certain time has passed
import os # [NP] This is used to obtain the parent (folder) file directory path for the game so we can access files within the folder itself

# IMPORT PY FILES =============================================================

from Order_Match import order_match
from Accuracy_Function import accuracy_as_percent

# ASSET CALL ==================================================================

parentfile = os.path.dirname(__file__) # [NP] Find the path for the parent folder

# [NP] Call all image files
HAM = r"" + parentfile + "\Images\GooseJordan.png"
MAT = r"" + parentfile + "\Images\GooseMatheus.png"
PEND = r"" + parentfile + "\Images\GoosePendar.png"
NICK = r"" + parentfile + "\Images\GooseNP.png"
ZINO = r"" + parentfile + "\Images\GooseZino.png"
HELMET = r"" + parentfile + "\Images\GooseEng.png"
KATIE = r"" + parentfile + "\Images\GooseKY.png"
LAW = r"" + parentfile + "\Images\GooseLAW.png"
GLIAM = r"" + parentfile + "\Images\GooseLG.png"
KAMKAR = r"" + parentfile + "\Images\Machine.png"
Speech = r"" + parentfile + "\Images\Speech-Bubble.png"
Background = r"" + parentfile + "\Images\Background.png"
MachineIMG = r"" + parentfile + "\Images\Machine.png"
FlaskA = r"" + parentfile + "\Images\FlaskA.png"
FlaskB = r"" + parentfile + "\Images\FlaskB.png"
FlaskC = r"" + parentfile + "\Images\FlaskC.png"

# OPTION LISTINGS =============================================================

Greeting = ['Hello', 'Hows it going', 'Hi']  # [LAW] List of greetings
Chemicals = ["NaCl (Sodium Chloride)", "NH3 (Ammonia)", "NH4OH (Ammonium Hydroxide)", "HCl (Hydrochloric Acid)", "NaOH (Sodium Hydroxide)"] # [NP] List of possible chemicals to receive in an order

 # [LAW] Instructions for each order
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

ChemicalCorrelator = {"H2O (Water)": FlaskC, "NH3OH (Ammonia Hydroxide)": FlaskB, "NH4 (Ammonium)": FlaskB} # [NP] Matches each chemical with an appropriate sprite
Pics = [HAM, MAT, PEND, NICK, ZINO, HELMET, KATIE, LAW, GLIAM, KAMKAR]  # [LAW] List of geese
instruction_list=[NaClin,NH3in,NH4OHin,HClin,NaOHin] # [NP] Puts all the instructions into a list which has the same indexes as Chemicals for its respective elements
DefaultFlask = FlaskA # [NP] If a chemical isn't found in the correlator above, it will be matched with this flask instead

# GAME SETTINGS ===============================================================

QuantityRange = [1, 999] # [NP] The range of quantity of a chemical a customer can order
TextFont = "Calibri" # [NP] The font the game uses
CustomerSpeed = 1 # [NP] Multiplies the customer walk speed
FlaskSpeed = 1 # [NP] Multiplies the flask conveyor speed
CustomerSpeakTimer = 0.25 # [NP] The delay between the customer arriving and the customer saying their order

# UI SIZE VALUES ==============================================================

ScreenSize = (1300, 800)
SpeechBubbleSize = (550, 550)
MachineSize = (1300, 800)
FlaskSize = (200, 250)
FontSizes = [40, 25]

BigCLSize = [700, 400, 50, 50] 
SmallCLSize = [700, 50, 50, 50]
BigButtonSize = [1000, 750, 250, 60]
SmallButtonSize = [1000, 650, 250, 60]

# UI POSITION VALUES ==========================================================

FlaskStartingPos = (850, 90)
FlaskCopyPos = (650, 90)
BackgroundPos = (0, 0)
MachinePos = (0, 0)
SpeechBubblePos = (700, 10)
ScorePos = (1010, 760)
AcceptButtonFontPos = (1010, 760)
QuitButtonFontPos = (1010, 660)

OrderAFontPos = [760, 150]
OrderBFontPos = [760, 190]
InstructionsFontPos = [30, 250]

CustomerOffset = 1.5 # [NP] How much the customer moves per frame
FlaskOffset = 10 # [NP] How much the flask moves per frame

# FRAME SETTINGS ==============================================================

MoveFrames = 50 # [NP] How many frames the flask moves in before the next customer comes in
CustomerFrameRate = 30
MachineFrameRate = 10

# COLOURS =====================================================================

BLACK = (0, 0, 0)
RED = (225, 0, 0)
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)

# STARTING THE GAME ===========================================================

def Game(Score): # [NP] The score parameter determines how much score the player has

# TEXT FUNCTIONS ==============================================================    

    # [LAW] Order text function
    def display_text(text, x, y):
        font.render_to(screen, (x, y), text, BLACK)

    def display_text2(text, x, y):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            font2.render_to(screen, (x, y + i * 30), line.strip(), BLACK)

# START-UP ====================================================================

    pygame.init() # [NP] Initializes the game
    screen = pygame.display.set_mode(ScreenSize) # [LAW] Sets the size of the screen
    clock = pygame.time.Clock() # [LAW] Creates a Pygame clock to control frame rates
    
# LOADING FONTS ===============================================================

    # [LAW] Sets the font and size of the text
    font = pygame.freetype.SysFont(TextFont, FontSizes[0])
    font2 = pygame.freetype.SysFont(TextFont, FontSizes[1])

# LOADING SPRITES =============================================================

    background = pygame.image.load(Background).convert_alpha() # [LAW] Loads and converts the background image
    speech_bubble = pygame.image.load(Speech).convert_alpha() # [LAW] Loads and converts the speech bubble image
    Machine = pygame.image.load(MachineIMG).convert() # [NP] Loads and converts the machine image
    
# LOADING BUTTONS =============================================================

    # [NP] Define the click area properties
    click_area = pygame.Rect(BigCLSize[0], BigCLSize[1], BigCLSize[2], BigCLSize[3])
    click_area2 = pygame.Rect(SmallCLSize[0], SmallCLSize[1], SmallCLSize[2], SmallCLSize[3])
    click_area3 = pygame.Rect(BigCLSize[0], BigCLSize[1], BigCLSize[2], BigCLSize[3])
    
    # [LAW] Define the button properties
    button_rect = pygame.Rect(BigButtonSize[0], BigButtonSize[1], BigButtonSize[2], BigButtonSize[3])  # [LAW] Position the first button
    button_rect2 = pygame.Rect(SmallButtonSize[0], SmallButtonSize[1], SmallButtonSize[2], SmallButtonSize[3])  # [LAW] Position the second button
    
# ALTERING SCALES =============================================================

    speech_bubble = pygame.transform.scale(speech_bubble, SpeechBubbleSize)  # [LAW] Resizes the speech bubble
    Machine = pygame.transform.scale(Machine, MachineSize)  # [LAW] Scale the background to fit the screen
    
# SETTING SCORES ==============================================================

    scorestr ='SCORE: ' + str(Score) # [NP] The score string gets created

# INITIALIZATING CONTROL VARIABLES ============================================

    # [LAW] Initializes control variables
    show_speech_bubble = False
    running = True
    show_machine = False
    Show_things = False
    show_instructions = False
    Show_FlaskCOPY = False
    Move_Flask = False
    FlaskMoves = MoveFrames // FlaskSpeed
    
# CUSTOMER CREATION ===========================================================
    
    GooseCustomer = random.choice(Pics)  # [LAW] Selects a random goose
    player = pygame.image.load(GooseCustomer).convert_alpha()  # [LAW] Loads and converts the goose image
    position = player.get_rect()  # [LAW] Gets the position of the player

# ORDER CREATION ==============================================================

    orderchem = Chemicals[random.randint(0, len(Chemicals) - 1)] # [NP] Selects a random chemical
    ordercapacity = random.randint(QuantityRange[0], QuantityRange[1]) # [NP] Selects a random quantity

    OrderA = random.choice(Greeting) + " " + "I Need " + str(ordercapacity)   # [LAW] Order with random greeting and a random chemical
    OrderB = "moles of " + str(orderchem)
    
# LOADING INSTRUCTIONS ========================================================

    for i in range(len(Chemicals)): # [LAW] Finds what Chemical has been ordered and assigns the instructions to the instructions variable
        if Chemicals[i] in orderchem:
            instructions = instruction_list[i]
            
# LOADING FLASKS ==============================================================

    if orderchem in ChemicalCorrelator: FlaskIMG = ChemicalCorrelator[orderchem] # [NP] Finds the chemical's corresponding sprite
    else: FlaskIMG = DefaultFlask # [NP] If not found in Correlator, use the default flask instead
    
    Flask = pygame.image.load(FlaskIMG).convert_alpha()  # [LAW] Load and convert the Flask image with alpha for transparency
    FlaskCOPY = Flask.copy()  # [LAW] Make a copy of Flask for FlaskCOPY

    Flask = pygame.transform.scale(Flask, FlaskSize)  # [LAW] Adjust the dimensions as needed
    FlaskCOPY = pygame.transform.scale(FlaskCOPY, FlaskSize)  # [LAW] Make FlaskCOPY smaller

    flask_position= Flask.get_rect()
    flask_position.topleft = FlaskStartingPos  # [LAW] Set the starting position of the flask

# CUSTOMER MOVEMENT ===========================================================

    # [LAW] Main display loop
    for x in range(100 // CustomerSpeed):  # [LAW] This tells the following to repeat 100 times
        screen.blit(background, BackgroundPos)  # [LAW] Ensures background is drawn before everything else
        position = position.move(CustomerOffset * CustomerSpeed, 0)  # [LAW] Moves the player
        screen.blit(player, position)  # [LAW] Draws the player in the new position
        pygame.display.update()  # [LAW] Updates the display
        clock.tick(CustomerFrameRate)  # [LAW] Sets the frame rate

# PYGAME UPDATE LOOP ==========================================================

    start_time = time.time() # [LAW] Initializes timer
    while running:
        
# UPDATING UI =================================================================

        screen.blit(background, BackgroundPos)  # [LAW] Redraws the background
        screen.blit(player, position)  # [LAW] Redraws the player at the current position
        
        # [LAW] Draw the first button
        pygame.draw.rect(screen, BLUE, button_rect) # [LAW] Creates a blue button
        font = pygame.freetype.SysFont(None, 36)
        font.render_to(screen, AcceptButtonFontPos, "Accept Order", WHITE) # [LAW] Adds white text

        # [LAW] Draw the second button
        pygame.draw.rect(screen, RED, button_rect2) # [LAW] Creates a red button
        font.render_to(screen, QuitButtonFontPos, "Quit", WHITE) # [LAW] Adds white text
        
# PYGAME EVENTS ===============================================================        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # [LAW] Allows the window to be closed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):  # [LAW] Check if the click is within the first button's area
                    Show_things = True
                    Show_FlaskCOPY = True
                elif button_rect2.collidepoint(mouse_pos):  # [LAW] Check if the click is within the second button's area
                    running= False
                elif click_area3.collidepoint(mouse_pos): # [NP] Check if the DONE button has been clicked
                    FlaskPhase = 0
                    Move_Flask = True
                    Show_FlaskCOPY = False
                 
                    # [KY] - call order match and accuracy as percent functions from Order_Match
                    Order_points = order_match(output, orderchem) 
                    Order_accuracy = accuracy_as_percent(output, orderchem)
                    
# UI CONDITIONALS =============================================================
                    
        # [LAW] Checks if enough seconds have elapsed
        if time.time() - start_time >= CustomerSpeakTimer: show_speech_bubble = True
            
        if Show_things: # [NP] Switches from Customer view to Machine view
            show_speech_bubble = False
            show_machine = True
            show_instructions = True

        # [LAW] Displays text and speech bubble after two seconds have passed
        if show_speech_bubble:
            screen.blit(speech_bubble, SpeechBubblePos)  # [LAW] Positions the speech bubble
            display_text(OrderA, OrderAFontPos[0], OrderAFontPos[1])  # [LAW] Adjusts text position to fit inside the speech bubble
            display_text(OrderB, OrderBFontPos[0], OrderBFontPos[1])

        if show_machine:
            
            # [LAW] Draw the mix Click Area
            pygame.draw.rect(screen, BLACK, click_area3)
            
            screen.blit(Machine, MachinePos) # [NP] Show the machine
            font.render_to(screen, ScorePos, scorestr, WHITE) # [NP] Show the player's current score
        
        if show_instructions: display_text2(instructions, InstructionsFontPos[0], InstructionsFontPos[1]) # [NP] Show the instructions
        
        if Show_FlaskCOPY: screen.blit(FlaskCOPY, FlaskCopyPos)  # [LAW] Display FlaskCOPY at the new position
            
        if Move_Flask:
            
            if FlaskPhase < FlaskMoves:
                flask_position.move_ip(FlaskOffset * FlaskSpeed, 0)  # [LAW] Move the Flask
                screen.blit(Flask, flask_position)  # [LAW] Draw Flask in the new position
            else:
                Game(Score + Bounty)
            FlaskPhase += 1
            
# RESETTING THE LOOP ==========================================================

        pygame.display.update() # [NP] Updates the pygame display
        clock.tick(MachineFrameRate)  # [LAW] Control the frame rate

# QUITTING THE GAME ===========================================================

    pygame.quit()  # [LAW] Quits Pygame after all the functions have been completed

# STARTING THE GAME ===========================================================

Game(0) # [NP] Plays The Game.

# END =========================================================================


