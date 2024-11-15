# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:32:49 2024

@authors:   Liam Gleason
            Nicholas Pribytkov
"""

# This script creates classes for each molecule/element and stores information regarding it
# Quantities can be edited here to store how much of each molecule we have
# All quantities are in MOLES

class Hydrogen:
    Compound = "H2"
    Quantity = 0

class Carbon:
    Compound = "C"
    Quantity = 0

class Oxygen:
    Compound = "O2"
    Quantity = 0
    
class Nitrogen:
    Compound = "N2"
    Quantity = 0

class Sodium:
    Compound = "Na"
    Quantity = 0

class Chlorine:
    Compound = "Cl"
    Compound = 0
    
class Calcium:
    Compound = "Ca"
    Compound = 0

class Water:
    Compound = "H20"
    Compound = 0


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:05:04 2024

@authors: Katie Yu
"""

#RECIPE CLASSES
#Quantity is only required if we want to use chemicals produced in other recipes
#Difficulty is not required if our only difficulty measure is the waiting time of geese
#We need to decide on these things :P

#Basic Recipes
class SodiumChloride:
    Name = "NaCl (Sodium Chloride)"
    Ingredients = ['Sodium','Chlorine']
    Difficulty = 'E'
    #Quantity = 0
    
    
class Ammonia:
    Name = "NH3 (Ammonia)"
    Ingredients = ['Hydrogen','Nitrogen']
    Difficulty = 'E'
    #Quantity = 0
    
    
class Hydrochloric Acid:
    Name = "HCl (Hydrochloric Acid)"
    Ingredients = ['Hydrogen','Chlorine','Water']
    Difficulty = 'M'
    #Quantity = 0
    
    
#Complex Recipes
class Ammonium Hydroxide:
    Name = "NH4OH (Ammonium Hydroxide)"
    Ingredients = ['Ammonia','Water']
    Difficulty = 'M'
    #Quantity = 0


class Sodium Hydroxide:
    Name = "NaOH (Sodium Hydroxide)"
    Ingredients = ['Sodium Chloride','Water']
    Difficulty = 'H'
    #Quantity = 0
    
#test: NaCl_recipe().Difficulty
