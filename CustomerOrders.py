# CUSTOMER ORDERS =============================================================

# The purpose of this file to generate orders for customers for the player
# to fulfill.

# Parent: Working Moving Goose ================================================
# Author: Nicholas Pribytkov ==================================================

# IMPORT PYTHON MODULES =======================================================

from random import * # [NP] This calls the random module, which let's the function obtain random numbers

# ORDER LIST ===============================================================

# [NP] The chemical list shows all possible chemicals that a customer can order
Chemicals = ["NaCl (Sodium Chloride)", "NH3 (Ammonia)", "NH4OH (Ammonium Hydroxide)", "HCl (Hydrochloric Acid)", "NaOH (Sodium Hydroxide)"]

# CUSTOMER ORDER ==============================================================
   
def CustomerOrder(): # [NP] Generates a Customer Order
    '''
    CUSTOMER ORDER
    Generates a customer order.

    Returns
    -------
    list
        [Quantity, Chemical]

    '''
    
    orderchem = Chemicals[randint(0, len(Chemicals) - 1)] # [NP] Picks a random chemical from the chemical list
    ordercapacity = randint(1, 999) # [NP] Picks a random quantity of the chemical
    
    return [str(ordercapacity), str(orderchem)] # [NP] Return the customer order details back

# END =========================================================================
