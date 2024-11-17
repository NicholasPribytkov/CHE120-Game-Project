#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:41:06 2024

@author: Katie1
"""
#Required = chemical_produced (non-existent rn), customer_orders, and molecules
#import all here

recipe_points = recipe.difficulty
time_points = 2 
#start with a low value for time_points since the player will have the most time to make the recipe

def order_match(chem_produced, chem_ordered):
    
    if chem_produced == chem_ordered[3]:
        #this compares the names of the chemical produced and the chemical ordered
        
            accuracy = (chem_produced_quantity/chem_ordered[1])
            #this compares the quantities of the chemical produced and the chemical ordered
            
            points_per_order = (recipe_points + time_points)*accuracy
            #sample points_per_order = (10 + 2)*0.8 = 9.6
            #second sample points_per_order = (20 + 6)*1 = 25

            return points_per_order
        
            chem_match = True
        
    else:
        chem_match = False
        #if the player makes the completely wrong chemical
            
        if chem_match == True:
            #make goose leave here
            #allow player to play again?

        if chem_match == False:
            points_per_order = 0

#put in main file
            total_points = order_match() + total_points
            print(total_points)
            time_points += 2 
#this accounts for the fact that each customer is willing to wait for less time (you must make recipes faster, so you earn more points as a result) 
            wait_time -= 2
