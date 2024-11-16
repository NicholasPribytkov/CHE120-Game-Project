#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:41:06 2024

@author: Katie1
"""
#Required = chemical_produced (non-existent rn), customer_orders, and molecules
#import all here

def order_match(chem_produced, chem_ordered):
    
    if chem_produced == chem_ordered[3]:
        chem_match = True 
        #this compares the names of the chemical produced and the chemical ordered
        
        if chem_match == True:
            accuracy = (chem_produced_quantity/chem_ordered[1])
            #this compares the quantities of the chemical produced and the chemical ordered
            
            recipe_points = recipe.difficulty
            points_per_order = (recipe_points + time_points)*accuracy
            #sample points_per_order = (10 + 2)*0.8 = 9.6
            #second sample points_per_order = (20 + 6)*1 = 25

           
            return points_per_order
        
            order_complete = True
        
    else:
        chem_match == False
            
        if order_complete == True:
            #make goose leave here
            #allow player to play again?
    
            total_points = ''
            print(total_points)
            time_points += 2 
#this accounts for the fact that each customer is willing to wait for less time (you must make recipes faster, so you earn more points as a result) 
            wait_time -= 2
