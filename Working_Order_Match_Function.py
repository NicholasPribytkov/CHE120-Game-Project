
# WORKING ORDER MATCH FUNCTION ================================================

# This file compares the types of objects, which checks how much chemicals are
# produced, and how much chemicals the customer ordered. This file checks 
# to make sure the correct quantity and type are given. This file is also
# responsible for giving out failure penalties and tracks customer wait
# time.

# Parent: main ================================================================
# Author: Katie Yu ============================================================
# Editor(s): Nicholas Pribytkov ===============================================

def order_match(chem_in, chem_desired):
# [KY] Default arguments allow us to compare the variables from the previous two functions
# [KY] Variables from previous two functions are chem_produced and chem_ordered
    
    if type(chem_in) == type(chem_desired):
        # [KY] This compares the names of the chemical produced and the chemical ordered
        
        chem_match = True
        # [KY] Take abs value of error
        accuracy = abs((chem_in.quantity - chem_desired.quantity)/chem_desired.quantity)
        # [KY] If customer orders 2 mol and you make 1.75, accuracy = 0.875

        accuracy_percent = accuracy*100
            
        points_per_order = int(chem_desired.difficulty + time_difference)*accuracy
        # [KY] Sample points_per_order = (20 + (20-10))*0.8 = 24
        
        return points_per_order
        return accuracy_percent
        # [KY] Accuracy should be very low for a fail to occur
        # Use accuracy to determine fail
        
    else:
        chem_match = False
        points_per_order = 0
        accuracy_percent = 0
        accuracies_below_30 += 1
        
        # [KY] If the player makes the completely wrong chemical
            
        if chem_match == True:
            # [KY] Make goose leave here (happy)

        if chem_match == False:
            # [KY] Make goose leave here (sad)

# [KY] Put in main file
            # time_points = 2 
            # [KY] initialize time_points (if this is what we want)
            # [KY] Start with a low value for time_points since the player will have the most time to make the recipe
            
            total_points += points_per_order
            return total_points
