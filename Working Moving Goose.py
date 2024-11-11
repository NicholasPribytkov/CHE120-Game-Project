import pygame  # LAW main game functions
import random  # LAW This is used to randomize things
import pygame.freetype  # LAW This is used for the text on the screen
import time  # LAW used for text showing up after a certain time has passed

# LAW Initializes the Pygame
pygame.init()

# LAW Define file paths of the geese
HAM = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose4.png"
MAT = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose5.png"
PEND = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose6.png"
NICK = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose7.png"
ZINO = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose8 (1).png"
HELMET = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose8.png"
KATIE = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose9.png"
LAW = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose1.png"
GLIAM = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose2.png"
KAMKAR = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose3.png"
Speech = r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Speech-Bubble.png"

# LAW Initializes Goose Ordering components 
Pics = [HAM, MAT, PEND, NICK, ZINO, HELMET, KATIE, LAW, GLIAM, KAMKAR]  # LAW List of geese
a = random.choice(Pics)  # LAW Selects a random goose

Greeting = ['Hello', 'Hows it going', 'Hi']  # LAW List of greetings
Chem = ['a', 'b', 'c']  # LAW List of chemicals
Order = random.choice(Greeting) + ' I would like ' + random.choice(Chem)  # LAW Order with random greeting and a random chemical

screen = pygame.display.set_mode((1300, 800))  # LAW Sets the size of the screen
clock = pygame.time.Clock()  # LAW Creates a Pygame clock to control frame rates

player = pygame.image.load(a).convert_alpha()  # LAW Loads and converts the goose image
background = pygame.image.load(r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\R.png").convert_alpha()  # LAW Loads and converts the background image
speech_bubble = pygame.image.load(Speech).convert_alpha()  # LAW Loads and converts the speech bubble image
speech_bubble= pygame.transform.scale(speech_bubble, (550,550))# LAW Resizes the speech bubble

position = player.get_rect()  # LAW Gets the position of the player

# LAW Defines colors
BLACK = (0, 0, 0)

# Set up the font
font = pygame.freetype.SysFont("Calibri", 40)  # LAW Sets the font and size of the text

# LAW Main display loop
for x in range(100):# LAW This tells the following the repeat 100 times
    screen.blit(background, (0, 0))  # LAW Ensures background is drawn before everything else
    position = position.move(1.5, 0)  # LAW Moves the player
    screen.blit(player, position)  # LAW Draws the player in the new position
    pygame.display.update()  # LAW Updates the display
    clock.tick(30)  # LAW Sets the frame rate

# LAW Order text function
def display_text(text, x, y):
    font.render_to(screen, (x, y), text, BLACK)

# LAW Initializes timer and control variables
start_time = time.time()
show_text = False
show_speech_bubble = False
running = True

# LAW Main text loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # LAW Allows the window to be closed

    # LAW Checks if 1.25 seconds have elapsed
    if not show_text and time.time() - start_time >= 1.25:
        show_text = True
        show_speech_bubble = True

    screen.blit(background, (0, 0))  # LAW Redraws the background
    screen.blit(player, position)  # LAW Redraws the player at the current position

    # LAW Displays text and speech bubble after two seconds have passed
    if show_speech_bubble:
        screen.blit(speech_bubble, (700, 10))  #LAW Position the speech bubble
        display_text(Order, 780, 150)  #LAW Adjusts text position to fit inside the speech bubble

    # LAW Updates the display with this text
    pygame.display.update()
    clock.tick(10)  #LAW Control the frame rate

pygame.quit()  # LAW Quits Pygame after all the functions have been completed

    
