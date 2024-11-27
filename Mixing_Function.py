# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:30:36 2024

@author: liamg
"""
import Molecules as mol



def Mixing (mix1,mix2,mix3):
    NaCl = mol.NaCl()
    NH3 = mol.NH3()
    NH4OH = mol.NH4OH()
    HCl = mol.HCl()
    NaOH = mol.NaOH()

    if mix3 == None and not type(mix1) == None and not type(mix2) == None: # [LG] Identifies if there are two or three ingridents
        print("loop1")
        mixture = [mix1.Name, mix2.Name] # [LG] Makes a list of the names of the ingridents
        mixture_set = set([mix1.Name, mix2.Name]) # [LG] Makes a set to allow for checking against other ingreident sets regardless of order
        if mixture_set == set(NaCl.Ingredients): # [LG] checks if the ingridents of the product are the same as the provided ingridents
            for i in range (len(NaCl.Ingredients)):
                if NaCl.Ingredients[i]==mix1.Name:
                    mix1ratio = NaCl.Ingredient_ratios[i]
            for i in range (len(NaCl.Ingredients)):
                if NaCl.Ingredients[i]==mix2.Name: # [LG] checks if the ingridents of the product are the same as the provided ingridents
                    mix2ratio = NaCl.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity / mix1ratio # [LG] Idenitfies stoichometric values of each compound/attom
            mix2Stoich = mix2.Quantity / mix2ratio
            if mix1Stoich >= mix2Stoich: # [LG] Chceks what limiting reactant is
                output = mol.NaCl() # [LG] Creates new mixture based on ingredients
                output.Quantity =+ round(mix2Stoich,2) # [LG] Applies quanitity to new mixture according limiting reactant
                return output
            else:
                output = mol.NaCl()
                output.Quantity =+ round(mix1Stoich,2)
                return output
        elif mixture_set == set(NH3.Ingredients): # [LG] repeat as before but with different ingredients
            for i in range (len(NH3.Ingredients)):
                if NH3.Ingredients[i]==mix1.Name:
                    mix1ratio = NH3.Ingredient_ratios[i]
            for i in range (len(NH3.Ingredients)):
                if NH3.Ingredients[i]==mix2.Name: 
                    mix2ratio = NH3.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity / mix1ratio
            mix2Stoich = mix2.Quantity / mix2ratio
            if mix1Stoich >= mix2Stoich:
                output = mol.NH3()
                output.Quantity =+ round(mix2Stoich,2)
                return output
            else:
                output = mol.NaCl()
                output.Quantity =+ round(mix1Stoich,2)
                return output
        elif mixture_set == set(HCl.Ingredients): # [LG] repeat as before but with different ingredients
            print("HCL PROCK")
            for i in range (len(HCl.Ingredients)):
                if HCl.Ingredients[i]==mix1.Name:
                    mix1ratio = HCl.Ingredient_ratios[i]
            for i in range (len(HCl.Ingredients)):
                if HCl.Ingredients[i]==mix2.Name:
                    mix2ratio = HCl.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity / mix1ratio
            mix2Stoich = mix2.Quantity / mix2ratio
            if mix1Stoich >= mix2Stoich:
                output = mol.HCl()
                output.Quantity =+ round(mix2Stoich,2)
                return output
            else:
                output = mol.NaCl()
                output.Quantity =+ round(mix1Stoich,2)
                return output
        else:
            return None
        
    elif not mix3 == None: # [LG] Determines if mix3 has been assigned to somthing
        mixture_set = set([mix1.Name,mix2.Name,mix3.Name]) # [LG] makes a set of all the ingridents provided (mixture inputs)
        if mixture_set == set(NH4OH.Ingredients): # [LG] Checks if the provided ingrediets are the same as needed ot make the new mix
            for i in range (len(NH4OH.Ingredients)): # [LG] Finds the stoichiometric coeficent for first ingrident
                if NH4OH.Ingredients[i] == mix1.Name:
                    mix1ratio = NH4OH.Ingredient_ratios[i] 
            for i in range (len(NH4OH.Ingredients)): # [LG] finds stoichiometric coeficent for seccond ingrident
                if NH4OH.Ingredients[i] == mix2.Name:
                    mix2ratio = NH4OH.Ingredient_ratios[i]
            for i in range (len(NH4OH.Ingredients)): # [LG] finds stoichiometric coeficent for third ingrident
                if NH4OH.Ingredients[i] == mix3.Name:
                    mix3ratio = NH4OH.Ingredient_ratios[i]
            mix1Stoich = mix1.Quantity/mix1ratio # [LG] determines stoichiometric ratio for first ingrident
            mix2Stoich = mix2.Quantity/mix2ratio# [LG] determines stoichiometric ratio for  seccond ingrident
            mix3Stoich = mix3.Quantity/mix3ratio# [LG] determines stoichiometric ratio for third ingrident
            if mix1Stoich <= mix2Stoich and mix1Stoich <= mix3Stoich: # [LG] checks if mix1 ratio is the smallets
                output = mol.NH4OH()
                output.Quantity += round(mix1Stoich,2) # [LG] Applies mix1 ratio to quantity for new mix
                return output
            elif mix2Stoich <= mix1Stoich and mix2Stoich <= mix2Stoich: # [LG] checks if mix2 ratio is the smallest
                output = mol.NH4OH()
                output.Quantity += round(mix2Stoich,2) # [LG] applies mix2 ratio to quantity for new mix
                return output
            else:
                output = mol.NH4OH()
                output.Quantity += round(mix3Stoich,2) # [LG] applies mix3 ratio to quanitity for new mix
                return output

        elif mixture_set == set(NaOH.Ingredients): # [LG] same for new recipe
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
            if mix1Stoich <= mix2Stoich and mix1Stoich <= mix3Stoich:
                output = mol.NaOH()
                output.Quantity =+ round(mix1Stoich,2)
                return output
            elif mix2Stoich <= mix1Stoich and mix2Stoich <= mix2Stoich:
                output = mol.NaOH()
                output.Quantity += round(mix2Stoich,2)
                return output
            else:
                output = mol.NaOH()
                output.Quantity += round(mix3Stoich,2)
                return output
        else:
            return None # [LG] if mix3 is not None and doesnt fit a recipe return None
    else:
        
        return None # [LG] if mix3 is None and mix1 and mix2 dont make a recipe return none, OR if mix1 or mix2 are None return None
        

