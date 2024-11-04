# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:56:39 2024

@author: Nicholas Pribytkov
"""
import CustomerOrders

MyChemicals = ["", "", ""]
MyChemicals[0] = input("What chemical is that?")
MyChemicals[1] = input("What unit?")
MyChemicals[2] = input("What is your quantity?")

CustomerOrders.OrderUp()

print(MyChemicals)
