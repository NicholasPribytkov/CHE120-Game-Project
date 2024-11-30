# ACCURACY FUNCTION ===========================================================

# This file is a function that determines the accuracy percent of the quantity
# of the inputted chemical compared to the quantity of the chemical that 
# is desired in the order.

# Parent: GooseUpdates ========================================================
# Author: Katie Yu ============================================================
# Editor(s): Nicholas Pribytkov ===============================================

# FUNCTION ====================================================================

def accuracy_as_percent(chem_made, chem_desired, chem_made_quantity, chem_desired_quantity):
    
        # [NP] chem_made represents the chemical produced and chem_desired is the chemical ordered

        if type(chem_made) == type(chem_desired): # [NP] Check if the player chemical and the order chemical are the same
            if chem_made_quantity <= 2*chem_desired_quantity:
                accuracy_percent = (1 - abs(chem_made_quantity - chem_desired_quantity)/chem_desired_quantity) * 100
                
                # [KY] absolute value accounts for the user making either too much or too little of a chemical (so 7 mols produced and 5 mols ordered would return same accuracy as 3 mols produced and 5 mols ordered)
                # [KY] Sample accuracy: if customer orders 2 mol and you make 1.75, accuracy = 0.875
            
            elif chem_made_quantity > 2*chem_desired_quantity:
                    accuracy_percent = 0
                    
                # [KY] prevents function from returning a negative accuracy value if you make more than double the amount ordered
                    
        else:
            accuracy_percent = 0
            
            # [KY] If the player makes the completely wrong chemical, accuracy is automatically 0
            
        return accuracy_percent

# END =========================================================================
