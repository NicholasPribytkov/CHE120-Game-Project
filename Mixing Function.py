# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:30:36 2024

@author: liamg
"""
import Molecules as mol

mix = mol.H()
mix.Quantity =+2
print(mix.Quantity)



def Mixing (mix1,mix2,mix3):
    NaCl = mol.NaCl()
    NH3 = mol.NH3()
    NH4OH = mol.NH4OH()
    HCl = mol.HCl()
    NaOH = mol.NaOH()

    if mix3 == None and not type(mix1) == None and not type(mix2) == None: # [LG] Identifies if there are two or three ingridents

        mixture = [mix1.Name, mix2.Name] # [LG] Makes a list of the names of the ingridents
        mixture_set = set[mix1.Name, mix2.Name] # [LG] Makes a set to allow for checking against other ingreident sets regardless of order
        if mixture_set == set(NaCl.Ingredients): # [LG] checks if the ingridents of the product are the same as the provided ingridents
            for i in range (len(NaCl.Ingredients)):
                if NaCl.Ingredients[i]==mix1.Name:
                    mix1ratio = NaCl.Ingredient_ratios[i]
            for i in range (len(NaCl.Ingredients)):
                if NaCl.Ingredients[i]==mix2.Name: # [LG] checks if the ingridents of the product are the same as the provided ingridents
                    mix2ratio = NaCl.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity / mix1ratio
            mix2Stoich = mix2.Quantity / mix2ratio
            if mix1Stoich >= mix2Stoich:
                output = mol.NaCl()
                output.Quantity =+ mix2Stoich
                return output
            else:
                output = mol.NaCl()
                output.Quantity =+ mix1Stoich
                return output
        elif mixture_set == set(NH3.Ingredients): # [LG] checks if the ingridents of the product are the same as the provided ingridents
            for i in range (len(NH3.Ingredients)):
                if NH3.Ingredients[i]==mix1.Name:
                    mix1ratio = NH3.Ingredient_ratios[i]
            for i in range (len(NH3.Ingredients)):
                if NH3.Ingredients[i]==mix2.Name: # [LG] checks if the ingridents of the product are the same as the provided ingridents
                    mix2ratio = NH3.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity / mix1ratio
            mix2Stoich = mix2.Quantity / mix2ratio
            if mix1Stoich >= mix2Stoich:
                output = mol.NH3()
                output.Quantity =+ mix2Stoich
                return output
            else:
                output = mol.NaCl()
                output.Quantity =+ mix1Stoich
                return output
        elif mixture_set == set(HCl.Ingredients): # [LG] checks if the ingridents of the product are the same as the provided ingridents
            for i in range (len(HCl.Ingredients)):
                if HCl.Ingredients[i]==mix1.Name:
                    mix1ratio = HCl.Ingredient_ratios[i]
            for i in range (len(HCl.Ingredients)):
                if HCl.Ingredients[i]==mix2.Name: # [LG] checks if the ingridents of the product are the same as the provided ingridents
                    mix2ratio = HCl.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity / mix1ratio
            mix2Stoich = mix2.Quantity / mix2ratio
            if mix1Stoich >= mix2Stoich:
                output = mol.HCl()
                output.Quantity =+ mix2Stoich
                return output
            else:
                output = mol.NaCl()
                output.Quantity =+ mix1Stoich
                return output
        else:
            return None
        
    elif not type(mix3) == None:
        mixture = [mix1.Name,mix2.Name,mix3.Name]
        mixture_set = set(mixture)
        if mixture_set == set(NH4OH.Ingredients):
            for i in range (len(NH4OH.Ingredients)):
                if NH4OH.Ingredients[i] == mix1.Name:
                    mix1ratio = NH4OH.Ingredient_ratios[i]
            for i in range (len(NH4OH.Ingredients)):
                if NH4OH.Ingredients[i] == mix2.Name:
                    mix2ratio = NH4OH.Ingredient_ratios[i]
            for i in range (len(NH4OH.Ingredients)):
                if NH4OH.Ingredients[i] == mix3.Name:
                    mix3ratio = NH4OH.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity/mix1ratio
            mix2Stoich = mix2.Quantity/mix2ratio
            mix3Stoich = mix3.Quantity/mix3ratio
            if mix1Stoich >= mix2Stoich and mix1Stoich >= mix3Stoich:
                output = mol.NH4OH()
                output.Quantity =+ mix1Stoich
                return output
            elif mix2Stoich >= mix1Stoich and mix2Stoich >= mix2Stoich:
                output = mol.NH4OH()
                output =+ mix2Stoich
                return output
            else:
                output = mol.NH4OH()
                output =+ mix3Stoich
                return output
        elif mixture_set == set(NaOH.Ingredients):
            for i in range (len(NaOH.Ingredients)):
                if NaOH.Ingredients[i] == mix1.Name:
                    mix1ratio = NaOH.Ingredient_ratios[i]
            for i in range (len(NaOH.Ingredients)):
                if NaOH.Ingredients[i] == mix2.Name:
                    mix2ratio = NaOH.Ingredient_ratios[i]
            for i in range (len(NaOH.Ingredients)):
                if NaOH.Ingredients[i] == mix3.Name:
                    mix3ratio = NaOH.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity/mix1ratio
            mix2Stoich = mix2.Quantity/mix2ratio
            mix3Stoich = mix3.Quantity/mix3ratio
            if mix1Stoich >= mix2Stoich and mix1Stoich >= mix3Stoich:
                output = mol.NaOH()
                output.Quantity =+ mix1Stoich
                return output
            elif mix2Stoich >= mix1Stoich and mix2Stoich >= mix2Stoich:
                output = mol.NaOH()
                output =+ mix2Stoich
                return output
            else:
                output = mol.NaOH()
                output =+ mix3Stoich
                return output
        else:
            return None
    else:
        return None
        
