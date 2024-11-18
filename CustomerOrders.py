# CUSTOMER ORDERS =============================================================

# The purpose of this file to generate orders for customers for the player
# to fulfill.

# Parent: Working Moving Goose ================================================
# Author: Nicholas Pribytkov ==================================================

# IMPORT PYTHON MODULES =======================================================

from random import * # [NP] This calls the random module, which let's the function obtain random numbers
import Molecules as mol #[LG] Imports all our different molecules and recipies to be used in functions
# ORDER LIST ===============================================================

# [NP] The chemical list shows all possible chemicals that a customer can order
Chemicals = ["NaCl (Sodium Chloride)", "NH3 (Ammonia)", "NH4OH (Ammonium Hydroxide)", "HCl (Hydrochloric Acid)", "NaOH (Sodium Hydroxide)"]
NaCl = mol.NaCl()
NH3 = mol.NH3()
NH4OH = mol.NH4OH()
HCl = mol.HCl()
NaOH = mol.NaOH()
Chemicals = [NaCl,NH3,NH4OH,HCl,NaOH] # [LG] generates a generic object of every recipie to ask the player for, and latter compare to what is produced


# CUSTOMER ORDER ==============================================================
   
def CustomerOrder(): # [NP] Generates a Customer Order
    '''
    CUSTOMER ORDER
    Generates a customer order.

    Returns
    -------
    Object with assigned quanity
        

    '''
    
    orderchem = Chemicals[randint(0, len(Chemicals) - 1)] # [NP] Picks a random chemical from the chemical list
    ordercapacity = randint(1, 999) # [NP] Picks a random quantity of the chemical
    orderchem.Quantity =+ ordercapacity # [LG] Assigns the Amount of desired product to the object
    return orderchem # [NP] Return the customer order details back

# END =========================================================================
mix = CustomerOrder()
print(type(mix))
print (mix.Quantity)