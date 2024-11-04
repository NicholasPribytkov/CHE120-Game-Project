# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:16:52 2024

@author: Nicholas Pribytkov
"""
from random import *

Chemicals = ["H2O (Water)", "CO2 (Carbon Dioxide)", "CH3OH (Methanol)", "C2H5OH (Ethanol)", "HCl (Hydrochloric acid)", "NO2 (Nitrogen dioxide)", "SO2 (Sulfur Dioxide)", "CO (Carbon Monoxide)", "CH2O (Formaldehyde)", "ClO4 (Perchorate)"]
orderchem = Chemicals[randint(0, len(Chemicals) - 1)]
    
Units = ["g", "mol"]
orderunit = Units[randint(0, len(Units) - 1)]

ordercapacity = randint(1, 10000)

if ordercapacity >= 1000:
    ordercapacity /= 1000
    ordercapacity = round(ordercapacity, 2)
    orderunit = "k" + orderunit

print("I NEED " + str(ordercapacity) + " " + str(orderunit) + " " + str(orderchem))