# CUSTOMER ORDERS =============================================================

# Parent: Working Moving Goose ================================================
# Author: Nicholas Pribytkov ==================================================

# IMPORT PYTHON MODULES =======================================================

from random import * # [NP] This calls the random module, which let's the function obtain random numbers

# ORDER LIST ===============================================================

# [NP] The chemical list shows all possible chemicals that a customer can order
Chemicals = ["H2O (Water)", "CO2 (Carbon Dioxide)", "CH3OH (Methanol)", "C2H5OH (Ethanol)", "HCl (Hydrochloric acid)", "NO2 (Nitrogen dioxide)", "SO2 (Sulfur Dioxide)", "CO (Carbon Monoxide)", "CH2O (Formaldehyde)", "ClO4 (Perchorate)"]
Units = ["g", "mol"] # [NP] The customer can decide which unit of measurement they wish to use

# CUSTOMER ORDER ==============================================================
   
def CustomerOrder(): # [NP] Generates a Customer Order
    '''
    CUSTOMER ORDER
    Generates a customer order.

    Returns
    -------
    list
        [Quantity, Unit, Chemical]

    '''
    orderchem = Chemicals[randint(0, len(Chemicals) - 1)] # [NP] Picks a random chemical from the chemical list
    orderunit = Units[randint(0, len(Units) - 1)] # [NP] Picks a random unit of measurement to use
    ordercapacity = randint(1, 10000) # [NP] Picks a random quantity of the chemical
    if ordercapacity >= 1000: # [NP] If the quantity exceeds 1000, the function will shorten it down by converting to kilos, which divides the value by 1000 (ex. 1200g --> 1.2kg)
        ordercapacity /= 1000
        ordercapacity = round(ordercapacity, 2)
        orderunit = "k" + orderunit
    return [str(ordercapacity), str(orderunit), str(orderchem)] # [NP] Return the customer order details back

# END =========================================================================
