#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:02:15 2024

@author: Katie1
"""

def accuracy_as_percent(chem_in, chem_desired):
        if type(chem_in) == type(chem_desired):
            accuracy_percent = (abs((chem_in.Quantity - chem_desired.Quantity)/chem_desired.Quantity))*100

        else:
            # [KY] If the player makes the completely wrong chemical, accuracy is automatically 0
            accuracy_percent = 0
        
        return accuracy_percent
        
        # [KY] Accuracy is used to determine a fail in the main file
        # [KY] Using a separate function to return accuracy allows us to call the specific function from this file to us