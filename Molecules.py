# MOLECULES ===================================================================

# This file is meant to be storage for the quantity of chemicals,
# allowing other files to call classes (chemicals) and retrieve quantities if
# need be.

# Parent: main ================================================================
# Author: Nicholas Pribytkov ==================================================
# Editors: Katie Yu ===========================================================

# ELEMENTS ====================================================================

# [NP] Elements are listed here:

#3 recipe difficulty levels
#[KY] quantities are zero by default
class H:
    Name = "H"
    Quantity = 0

class C:
    Name = "C"
    Quantity = 0

class O:
    Name = "O"
    Quantity = 0
    
class N:
    Name = "N"
    Quantity = 0

class Na:
    Name = "Na"
    Quantity = 0

class Cl:
    Name = "Cl"
    Quantity = 0
    
class Ca:
    Name = "Ca"
    Quantity = 0



# COMPOUNDS ===================================================================

# [NP] Compounds are listed here:
class H2O:
    Name = "H2O"
    Ingredients = ['H', 'O']
    Quantity = 0
    Difficulty = 20 #[KY] two basic ingredients, non 1:1 ratio
    Ingredient_ratios = [2,1]
    
class NaCl:
    Name = "NaCl"
    Ingredients = ['Na', 'Cl']
    Quantity = 0
    Difficulty = 10 #[KY] two basic ingredients, 1:1 ratio
    Ingredient_ratios = [1, 1]
    
class HCl:
    Name = "HCl"
    Ingredients = ['H', 'Cl']
    Quantity = 0
    Difficulty = 10 #[KY] two basic ingredients, 1:1 ratio
    Ingredient_ratios = [1, 1]
    
class NaOH:
    Name = "NaOH"
    Ingredients = ['Na', 'H', 'O']
    Quantity = 0
    Difficulty = 30 #[KY] one ingredient you have to make, 1:1:1 ratio
    Ingredient_ratios = [1, 1, 1]
    
# POLYATOMICS =================================================================
    
# [NP] Polyatomics are listed here:

class NH3:
    Name = "NH3"
    Ingredients = ['N', 'H']
    Quantity = 0
    Difficulty = 20 #[KY] two basic ingredients, non 1:1 ratio
    Ingredient_ratios = [3, 1/3]

class NH4OH:
    Name = "NH4OH"
    Ingredients = ['NH3', 'H', 'O']
    Quantity = 0
    Difficulty = 30 #[KY] one ingredient you have to make, 1:1:1 ratio
    Ingredient_ratios = [1, 2, 1]
    
# END =========================================================================
