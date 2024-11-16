# MOLECULES ===================================================================

# This file is meant to be storage for the quantity of chemicals,
# allowing other files to call classes (chemicals) and retrieve quantities if
# need be.

# Parent: main ================================================================
# Author: Nicholas Pribytkov ==================================================

# ELEMENTS ====================================================================

# [NP] Elements are listed here:

class H:
    Name = "Hydrogen"
    Quantity = 0

class C:
    Name = "Carbon"
    Quantity = 0

class O:
    Name = "Oxygen"
    Quantity = 0
    
class N:
    Name = "Nitrogen"
    Quantity = 0

class Na:
    Name = "Sodium"
    Quantity = 0

class Cl:
    Name = "Chlorine"
    Quantity = 0
    
class Ca:
    Name = "Calcium"
    Quantity = 0

class H20:
    Name = "Water"
    Quantity = 0
    Difficulty = 10

# COMPOUNDS ===================================================================

# [NP] Compounds are listed here:
    
class NaCl:
    Name = "Sodium Chlorine"
    Ingredients = ['Na', 'Cl']
    Quantity = 0
    Difficulty = 10
    Ingredient_ratios = [1]
    
class HCl:
    Name = "Hydrochloric Acid"
    Ingredients = ['H', 'Cl']
    Quantity = 0
    Difficulty = 20
    Ingredient_ratios = [1]
    
class NaOH:
    Name = "Sodium Hydroxide"
    Ingredients = ['NaCl', 'H20']
    Quantity = 0
    Difficulty = 30
    Ingredient_ratios = [1]
    
# POLYATOMICS =================================================================
    
# [NP] Polyatomics are listed here:

class NH3:
    Name = "Ammonia"
    Ingredients = ['N', 'H']
    Quantity = 10
    Ingredient_ratios = [3, 1/3]

class NH4OH:
    Name = "Ammonium Hydroxide"
    Ingredients = ['NH3', 'H2O']
    Quantity = 20
    Ingredient_ratios = [1]
    
# END =========================================================================
