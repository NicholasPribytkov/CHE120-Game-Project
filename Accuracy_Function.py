# ACCURACY FUNCTION ===========================================================

# This file is a function that determines the accuracy percent of the quantity
# of the inputted chemical compared to the quantity of the chemical that 
# is desired in the order.

# Parent: GooseUpdates ========================================================
# Author: Katie Yu ============================================================
# Editor(s): Nicholas Pribytkov ===============================================

# FUNCTION ====================================================================

def accuracy_as_percent(chem_in, chem_desired, a, b):
    
        # [NP] chem_in represents the chemical that the player has made and chem_desired is the chemical that is outlined in the order
        # [NP] a and b represent the quantities of the player chemical and the order chemical respectively (shortened to make it easier to see the formula)

        if type(chem_in) == type(chem_desired): # [NP] Check if the player chemical and the order chemical are the same
            accuracy_percent = (1 - abs(a - b) / b) * 100
            
        # [KY] absolute value accounts for the user making either too much or too little of a chemical
        # [KY] Sample accuracy: if customer orders 2 mol and you make 1.75, accuracy = 0.875
        
        else:
            
            # [KY] If the player makes the completely wrong chemical, accuracy is automatically 0
            accuracy_percent = 0
            
        return accuracy_percent

# END =========================================================================