# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:16:08 2024

@author: liama
"""
import pygame#LAW main game functions
import random#This is used to randomize things
import pygame.freetype#This is used for the texton the screen
HAM=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose4.png"
MAT=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose5.png"
PEND=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose6.png"
NICK=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose7.png"
ZINO=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose8 (1).png"
HELMET=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose8.png"
KATIE=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose9.png"
LAW=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose1.png"
GLIAM=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose2.png"
KAMKAR=r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\Goose3.png"
#LAW This is all the gooses-> Need to change to locations/ names of the files for final



Pics=[HAM,MAT,PEND,NICK,ZINO,HELMET,KATIE,LAW,GLIAM,KAMKAR]#LAW This is all of our geese in a list
a=random.choice(Pics)#LAW This selects a random goose from the list above
           
screen = pygame.display.set_mode((1300, 800))#LAW This sets the size of the screen

clock = pygame.time.Clock()#LAW This gets a pygame clock to control rates of things

player = pygame.image.load(a).convert_alpha()#LAW This converts the goose into pixels whichr the computer can read and the alpha part removes the background

background = pygame.image.load(r"C:\Users\liama\OneDrive\Desktop\UNI stuff\CHE 120 Comp\R.png").convert()#LAW Same as above just for the background
screen.blit(background, (0, 0))#LAW Position interms of layer

position=player.get_rect()#LAW Monitors position of player

pygame.init() #LAW Initiallizes the following comands

Greetings=['Hello', 'Hi', 'Whats up' ]
Chemical_orders= ['a','b','c']

Chem= random.choice(Chemical_orders)#LAW selects a random greeting from the list
Hi= random.choice(Greetings)#LAW Selects a random chemical from the list
#These currently dont work in the speech thingy it does not like the concatonated string(Str(Hi, 'I would like', Chem))
b='I would like'

font = pygame.freetype.SysFont("Calibri", 100) #LAW This is the font and size of the text
font.render_to(background, (100, 600), b, 'Black', 10000)#LAW This is the position and colour and what the text says


for x in range(100):                    
    screen.blit(background, position, position)
    position=position.move(3,0)
    screen.blit(player, position)
    pygame.display.update()
    clock.tick(10)#LAW This moves the goose from a position of (0,0) to (3,0) at a tick speed of 10

 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
#LAW This allows the window to be closed 
 

    
