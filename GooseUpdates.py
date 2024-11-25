
# GOOSE UPDATES ===============================================================

# This file acts as the backbone of the game. It's main purpose is to update
# the UI and both calls and runs game mechanic files.

# Author: Liam Westlake =======================================================
# Editor(s): Nicholas Pribytkov, Katie Yu, Liam Gleason =======================

# IMPORT PYTHON MODULES =======================================================

import pygame  # [LAW] main game functions
import random  # [LAW] This is used to randomize things
import pygame.freetype  # [LAW] This is used for the text on the screen
import time  # [LAW] used for text showing up after a certain time has passed
import os # [NP] This is used to obtain the parent (folder) file directory path for the game so we can access files within the folder itself

# IMPORT PY FILES =============================================================

from Point_Function import point_calculation # [NP] This function allows the game to calculate how many points should be given per order fulfillment
from Accuracy_Function import accuracy_as_percent # [NP] This function determines how accurate the player is when filling out an order
import Molecules as mol # [NP] This file allows us to store and retrieve various values from element classes
import Mixing_Function as mix # [NP] This function lets the player mix chemicals

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

ChemicalCorrelator = {"H2O (Water)": FlaskC, "NH4OH (Ammonium Hydroxide)": FlaskB, "NH3 (Ammonia)": FlaskB} # [NP] Matches each chemical with an appropriate sprite
ChemicalClassification = {"H2O (Water)": mol.H2O(), "NH4OH (Ammonium Hydroxide)": mol.NH4OH(), "NH3 (Ammonia)": mol.NH3(), "NaCl (Sodium Chloride)": mol.NaCl(), "HCl (Hydrochloric Acid)": mol.HCl(), "NaOH (Sodium Hydroxide)": mol.NaOH()}
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

# [KY] Position and center buttons that show up if the player has failed the game
playagain_rect = pygame.Rect(650, 400, 700, 100) 
playagain_rect.center = (650, 400)

endgame_rect = pygame.Rect(650, 400, 700, 100)
endgame_rect.center = (650, 550)

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

# DEFINING BUTTONS ============================================================

class Button(): # [LG] Creats a class of Button allowing easy button creation that does functions
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False): # [LG] takes in position and size of button, then what function to run on press, and if its a press and hold button
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = { #[LG] Provides default colors for button states
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height)) #[LG] Defines visual area of button
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height) # [LG] Defines where button is interactable

    def draw(self, screen): #[LG] function to draw the button on the screen
        pygame.draw.rect(screen, pygame.Color(self.fillColors['normal']), (self.x, self.y, self.width, self.height))
        font = pygame.freetype.SysFont("Calibri", 30)
        font.render_to(screen, (self.x + 10, self.y + 10), self.buttonText, pygame.Color('black'))

    def process(self, storage): #[LG] function to be ran in loop, actualy checks if button is clicked, and runs given function on click, also stores a value to be acted on (used for adding mols to mix)
        if storage == None:
                   
            mousePos = pygame.mouse.get_pos()
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    if self.onePress:
                        self.onclickFunction()
                    elif not self.alreadyPressed:
                        self.onclickFunction()
                        self.alreadyPressed = True
                else:
                    self.alreadyPressed = False
            return storage
         
        else:   
            mousePos = pygame.mouse.get_pos()
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    if self.onePress:
                        storage = self.onclickFunction(storage)
                    elif not self.alreadyPressed:
                        storage = self.onclickFunction(storage)
                        self.alreadyPressed = True
                else:
                    self.alreadyPressed = False
            return storage
        
# DEFINING FUNCTIONS FOR DISPENSING SUBSTANCES ================================

def add_mols_H(obj): #[LG] Runs a function that inputs an object, then either assigns it to an element and or adds 0.5 to it for each time its pressed
    if obj == None:
        obj = mol.H()
    obj.Quantity += 0.5 #[LG] If button held adds 0.5 per frame
    print(obj)
    print(obj.Quantity)
    return obj

def add_mols_C(obj):
    if obj == None:
        obj = mol.C()
    obj.Quantity += 0.5
    print(obj)
    print(obj.Quantity)
    return obj

def add_mols_O(obj):
    if obj == None:
        obj = mol.O()
    obj.Quantity += 0.5
    print(obj)
    print(obj.Quantity)
    return obj

def add_mols_N(obj):
    if obj == None:
        obj = mol.N()
    obj.Quantity += 0.5
    print(obj)
    print(obj.Quantity)
    return obj

def add_mols_Na(obj):
    if obj == None:
        obj = mol.Na()
    obj.Quantity += 0.5
    print(obj)
    print(obj.Quantity)
    return obj

def add_mols_Cl(obj):
    if obj == None:
        obj = mol.Cl()
    obj.Quantity += 0.5
    print(obj)
    print(obj.Quantity)
    return obj

def add_mols_Ca(obj):
    if obj == None:
        obj = mol.Ca()
    obj.Quantity += 0.5
    print(obj)
    print(obj.Quantity)
    return obj

def isthesame(mix, obj): # [LG] tells if the mix and object are the same type
    return type(mix) == type(obj)
# THE MIX FUNCTION ============================================================

def mixing_sequence(): # [LG] function that returns true to allow if statement to attivate after button press
    return True
        
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
            
# CREATING DISPENSING BUTTONS =================================================

    H_button = Button(400,200,200,50, "add Hydrogen", add_mols_H, True) #[LG] Creates buttons that can be held, that run the listed function when pressed
    C_button = Button(400,400,200,50, "add Carbon", add_mols_C, True)
    O_button = Button(400,600,200,50, "add Oxygen", add_mols_O, True)
    N_button = Button(400,800,200,50, "add Nitrogen", add_mols_N, True)
    Na_button = Button(500,400,200,50, "add Sodium", add_mols_Na, True)
    Cl_button = Button(500,600,200,50, "add Chlorine", add_mols_Cl, True)
    Ca_button = Button(500,800,200,50, "add Calcium", add_mols_Ca, True)
    Mixing_button = Button(700,400,200,50, "mixing time", mixing_sequence, False)
    
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
    
# DEFINE MIXING VARIABLES =====================================================

    mix1 = None
    mix2 = None
    mix3 = None
    
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
    mixing_start = False
    OrderOver = False
    OrderPoints = 0
    
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
        
# ELEMENT LIST INITALIZATION ==================================================

    elementlist = [mol.H, mol.C, mol.O, mol.N, mol.Na, mol.Cl, mol.Ca] # [LG] Creates a list of all basic element types
    processlist_mix1 = [H_button.process(mix1), C_button.process(mix1),O_button.process(mix1), # [LG] creates a list of the process commands for the buttons in the same order as basic element type list
     N_button.process(mix1), Na_button.process(mix1),Cl_button.process(mix1),Ca_button.process(mix1)]
    processlist_mix2 = [H_button.process(mix2), C_button.process(mix2),O_button.process(mix2), # [LG] creates a list of the process commands for the buttons in the same order as basic element type list
     N_button.process(mix2), Na_button.process(mix2),Cl_button.process(mix2),Ca_button.process(mix2)]
    processlist_mix3 = [H_button.process(mix3), C_button.process(mix3),O_button.process(mix3), # [LG] creates a list of the process commands for the buttons in the same order as basic element type list
     N_button.process(mix3), Na_button.process(mix3),Cl_button.process(mix3),Ca_button.process(mix3)]
    
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
        
# PYGAME EVENTS AND BUTTON EVENTS =============================================        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # [LAW] Allows the window to be closed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos) and not show_machine:  # [LAW] Check if the click is within the first button's area
                    Show_things = True
                    Show_FlaskCOPY = True
                elif button_rect2.collidepoint(mouse_pos) and not show_machine:  # [LAW] Check if the click is within the second button's area
                    running = False
                elif click_area3.collidepoint(mouse_pos) and show_machine: # [NP] Check if the DONE button has been clicked
                    FlaskPhase = 0
                    Move_Flask = True
                    Show_FlaskCOPY = False
                elif playagain_rect.collidepoint(mouse_pos) and OrderOver:
                    Game(0)
                elif endgame_rect.collidepoint(mouse_pos) and OrderOver:
                    running = False
                    
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

        if show_instructions: display_text2(instructions, InstructionsFontPos[0], InstructionsFontPos[1]) # [NP] Show the instructions

        if Show_FlaskCOPY: screen.blit(FlaskCOPY, FlaskCopyPos)  # [LAW] Display FlaskCOPY at the new position
        
        if show_machine:
            
# STARTING UP THE MIXER =======================================================
        
            if mixing_start:
                mix1 = mix.Mixing(mix1, mix2, mix3)
                mix2 = None
                mix3 = None
                mixing_start = False
                
                
            H_button.draw(screen) #[LG] Draws all the buttons on screen
            C_button.draw(screen)
            O_button.draw(screen)
            N_button.draw(screen)
            Na_button.draw(screen)
            Cl_button.draw(screen)
            Ca_button.draw(screen)
            Mixing_button.draw(screen)
            
            #Hydrgoen
            if isthesame(mix1,mol.H): # [LG] Checks if mix1 is already H
                H_button.process(mix1)
            elif isthesame(mix2,mol.H): # [LG] Checks if mix2 is already H
                H_button.process(mix2)
            elif isthesame(mix3,mol.H): # [LG] Checks if mix3 is already H
                H_button.process(mix3)
            else: # [LG] if none of the mixes are already H
                if mix1 == None: # [LG] if mix1 is unassigned, assign it to H
                    H_button.process(mix1)
                elif mix2 == None: # [LG] if mix2 is unassigned, assign it to H
                    H_button.process(mix2)
                elif mix3 == None: # [LG] if mix3 is unassigned, assign it to H
                    H_button.process(mix3)
                # [LG] If mix1-mix3 are filled, and non are H, dont process the button
                
            #Carbon [LG] same for Carbon
            if isthesame(mix1,mol.C):
                C_button.process(mix1)
            elif isthesame(mix2,mol.C):
                C_button.process(mix2)
            elif isthesame(mix3,mol.C):
                C_button.process(mix3)
            else:
                if mix1 == None:
                    C_button.process(mix1)
                elif mix2 == None:
                    C_button.process(mix2)
                elif mix3 == None:
                    C_button.process(mix3)
                
            #Oxygen [LG] same for oxygen
            if isthesame(mix1,mol.O):
                O_button.process(mix1)
            elif isthesame(mix2,mol.O):
                O_button.process(mix2)
            elif isthesame(mix3,mol.O):
                O_button.process(mix3)
            else:
                if mix1 == None:
                    O_button.process(mix1)
                elif mix2 == None:
                    O_button.process(mix2)
                elif mix3 == None:
                    O_button.process(mix3)
                
            #Nitrogen [LG] same for Nitrogen
            if isthesame(mix1,mol.N):
                N_button.process(mix1)
            elif isthesame(mix2,mol.N):
                N_button.process(mix2)
            elif isthesame(mix3,mol.N):
                N_button.process(mix3)
            else:
                if mix1 == None:
                    N_button.process(mix1)
                elif mix2 == None:
                    N_button.process(mix2)
                elif mix3 == None:
                    N_button.process(mix3)
                
            #Sodium [LG] same for Sodium
            if isthesame(mix1,mol.Na):
                Na_button.process(mix1)
            elif isthesame(mix2,mol.Na):
                Na_button.process(mix2)
            elif isthesame(mix3,mol.Na):
                Na_button.process(mix3)
            else:
                if mix1 == None:
                    Na_button.process(mix1)
                elif mix2 == None:
                    Na_button.process(mix2)
                elif mix3 == None:
                    Na_button.process(mix3)
                
            #Chlorine [LG] same for Chlorine
            if isthesame(mix1,mol.Cl):
                Cl_button.process(mix1)
            elif isthesame(mix2,mol.Cl):
                Cl_button.process(mix2)
            elif isthesame(mix3,mol.Cl):
                Cl_button.process(mix3)
            else:
                if mix1 == None:
                    Cl_button.process(mix1)
                elif mix2 == None:
                    Cl_button.process(mix2)
                elif mix3 == None:
                    Cl_button.process(mix3)
                
            #Calcium [LG] same for Calcium
            if isthesame(mix1,mol.Ca):
                Ca_button.process(mix1)
            elif isthesame(mix2,mol.Ca):
                Ca_button.process(mix2)
            elif isthesame(mix3,mol.Ca):
                Ca_button.process(mix3)
            else:
                if mix1 == None:
                    Ca_button.process(mix1)
                elif mix2 == None:
                    Ca_button.process(mix2)
                elif mix3 == None:
                    Ca_button.process(mix3)
            mixing_start = Mixing_button.process(None)
            
# STARTING UP THE MACHINE =====================================================

            # [LAW] Draw the mix Click Area
            pygame.draw.rect(screen, BLACK, click_area3)
            
            screen.blit(Machine, MachinePos) # [NP] Show the machine
            font.render_to(screen, ScorePos, scorestr, WHITE) # [NP] Show the player's current score
        
# FLASK CONVEYOR BELT =========================================================
            
        if Move_Flask:
            
            if FlaskPhase < FlaskMoves:
                flask_position.move_ip(FlaskOffset * FlaskSpeed, 0)  # [LAW] Move the Flask
                screen.blit(Flask, flask_position)  # [LAW] Draw Flask in the new position
            else:
                
# POINT ASSIGNMENT/FAIL CHECK =================================================
       
                Order_accuracy = accuracy_as_percent(orderchem, orderchem, ordercapacity, ordercapacity) # [KY] Assign accuracy of order to accuracy_as_percent function call
                OrderPoints = point_calculation(ChemicalClassification[orderchem].Difficulty, Order_accuracy / 100, 0) # [KY] Assign points per order to order_match function call
                
                if Order_accuracy < 30: # [KY] Checks if the accuracy of the amount produced compared to the amount ordered is below 30 (fail condition)
                    pygame.draw.rect(screen, BLUE, playagain_rect) # [KY] draws play again and quit game buttons (rects are defined above)
                    pygame.draw.rect(screen, RED, endgame_rect) 
                    font.render_to(screen, (360, 385), "Game Over - Click to Play Again", WHITE)
                    font.render_to(screen, (550, 535), "Quit Game", WHITE)
                    OrderOver = True
                else:
                     Game(Score + OrderPoints)
            FlaskPhase += 1
            
# RESETTING THE LOOP ==========================================================

        pygame.display.update() # [NP] Updates the pygame display
        clock.tick(MachineFrameRate)  # [LAW] Control the frame rate

# QUITTING THE GAME ===========================================================

    pygame.quit()  # [LAW] Quits Pygame after all the functions have been completed

# STARTING THE GAME ===========================================================

Game(0) # [NP] Plays The Game.

# END =========================================================================
