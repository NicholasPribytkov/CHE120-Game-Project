#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:10:42 2024

@author: Katie1
"""
#need chem_produced and chem_ordered from previous two functions
#default arguments
#ensure that it takes the correct input
#this version of order match compares the types 
#chem_in must be connected to the recipes in order to use the recipe difficulty value
#bring up max point system
#upload new order match function

recipe_points = chem_in.difficulty
time_points = 2 
#start with a low value for time_points since the player will have the most time to make the recipe

def order_match(chem_in=chem_produced, chem_desired=chem_ordered):
#default arguments allow us to compare the variables from the previous two functions
#variables from previous two functions are chem_produced and chem_ordered
    
    if type(chem_in) == type(chem_desired):
        #this compares the names of the chemical produced and the chemical ordered
        
        if chem_in.quantity <= chem_desired.quantity:
            accuracy = (chem_in.quantity/chem_desired.quantity)
            #if customer orders 2 mol and you make 1.75, accuracy = 0.875
            
        if chem_in.quantity > chem_desired.quantity:
            accuracy = ((2*chem_desired.quantity - chem_in.quantity)/chem_desired.quantity)
            #if customer orders 2 mol and you make 2.25, accuracy = 0.875
            
            points_per_order = (recipe_points + time_points)*accuracy
            #sample points_per_order = (10 + 2)*0.8 = 9.6
            #second sample points_per_order = (20 + 6)*1 = 25

            return points_per_order
        
            chem_match = True
        
    else:
        chem_match = False
        points_per_order = 0
        
        #if the player makes the completely wrong chemical
            
        if chem_match == True:
            #make goose leave here
            #allow player to play again?

        if chem_match == False:

#put in main file
            total_points = order_match() + total_points
            print(total_points)
            time_points += 2 
#this accounts for the fact that each customer is willing to wait for less time (you must make recipes faster, so you earn more points as a result) 
            wait_time -= 2
