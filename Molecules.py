# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:32:49 2024

@author: liamg
"""

class Hydrogen:
    def Molecule(somename, quantity):
        print(somename)
        print(quantity)
        somename.quantity = quantity
   
    def myinfo(self):
        print(self.myname() + " " + str(self.amount()) + "kg")
    def myname(self):
        return self.name
    
    def amount(self):
        return self.quantity

class Water:
    def Molecule(somename, name, quantity):
        somename.name = name
        somename.quantity = quantity
   
    def myinfo(self):
        print(self.myname() + " " + str(self.amount()) + "kg")
    def myname(self):
        return self.name
    
    def amount(self):
        return self.quantity

mix1 = Hydrogen.Molecule("H2", 3)
mix2 = Water("H2O", 2)