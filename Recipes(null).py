#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:05:04 2024

@authors: Katie Yu
#this file has been combined with molecules.py for now
"""

#RECIPE CLASSES
#Quantity is only required if we want to use chemicals produced in other recipes
#Difficulty is not required if our only difficulty measure is the waiting time of geese
#We need to decide on these things :P

#Basic Recipes
class NaCl_recipe:
    Name = "NaCl (Sodium Chloride)"
    Ingredients = ['Sodium','Chlorine']
    Difficulty = 'E'
    #Quantity = 0
    
    
class NH3_recipe:
    Name = "NH3 (Ammonia)"
    Ingredients = ['Hydrogen','Nitrogen']
    Difficulty = 'E'
    #Quantity = 0
    
    
class HCl_recipe:
    Name = "HCl (Hydrochloric Acid)"
    Ingredients = ['Hydrogen','Chlorine','Water']
    Difficulty = 'M'
    #Quantity = 0
    
    
#Complex Recipes
class NH4OH_recipe:
    Name = "NH4OH (Ammonium Hydroxide)"
    Ingredients = ['Ammonia','Water']
    Difficulty = 'M'
    #Quantity = 0


class NaOH_recipe:
    Name = "NaOH (Sodium Hydroxide)"
    Ingredients = ['Sodium Chloride','Water']
    Difficulty = 'H'
    #Quantity = 0
    
#Backup Recipes
    

#test: NaCl_recipe().Difficulty
