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

# COMPOUNDS ===================================================================

# [NP] Compounds are listed here:

class H20:
    Name = "Water"
    Ingredients = ['H', 'H', 'O']
    Quantity = 0
    
class NaCl:
    Name = "Sodium Chlorine"
    Ingredients = ['Na', 'Cl']
    Quantity = 0
    
class HCl:
    Name = "Hydrochloric Acid"
    Ingredients = ['H', 'Cl']
    Quantity = 0
    
class NaOH:
    Name = "Sodium Hydroxide"
    Ingredients = ['Na', 'O', 'H']
    Quantity = 0
    
# POLYATOMICS =================================================================
    
# [NP] Polyatomics are listed here:

class NH3:
    Name = "Ammonia"
    Ingredients = ['N','H', 'H', 'H']
    Quantity = 0

class NH4OH:
    Name = "Ammonium Hydroxide"
    Ingredients = ['N', 'H', 'H', 'H', 'H', 'O', 'H']
    Quantity = 0
    
# END =========================================================================