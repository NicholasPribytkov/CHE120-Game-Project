
#         ________   __________     __________    ___________  _________
#        /   ____/  /          \   /          \  /    ______/ |   ______|
#       |   /      |    ____    | |    ____    | \    \____   |  |______
#       |  |    _  |   |____|   | |   |____|   |  \______  \  |   ______|
#       |   \__| |  \__________/   \__________/    _____/  /  |  |______
#        \_______|                                |_______/   |_________|


# CHE120 Project By ===========================================================

# Nicholas Pribytkov
# Liam Gleason
# Liam Andrew Westlake
# Katie Yu

# Welcome to Geese Lab. You are asked to work at a
# chemical facility, where you talk to customers who wish to buy chemicals,
# track their orders, mix chemicals up and give them the chemicals they want!
# 
# Work carefully but vigilantly to give customers their desired chemicals and
# recieve $$$$$ the bag $$$$$$.
#
# The game ends if the accuracy of the amount produced is below 30% for three non consecutive orders or 
# if the time taken to complete one order exceeds the customer wait time, whichever comes first


# MAIN ========================================================================

# This file is the backbone of the game. It does not impact the game itself in
# any way, but it calls all other files (or modules) in sequence which allows
# the game to flow and function.

# Author: Nicholas Pribytkov
# Editors: Katie Yu ==================================================

# IMPORT PY FILES =============================================================

#[KY] import rest of files
import CustomerOrders
import Mixing_Function
import Molecules
import TheMachine
import Order_Match_Function
import WorkingMovingGoose # [NP] WorkingMovingGoose outputs visuals of the Customers and Orders

#[KY] import pygame for end of game messages
import pygame
import pygame.freetype
#import TheMachine # [NP] TheMachine outputs visuals of the Machine at work, allowing the player to interface with it in order to mix chemicals together.

player, position, OrderA, OrderB, Order1, Order2 = WorkingMovingGoose.Customer()
b = WorkingMovingGoose.Runtime(player, position, OrderA, OrderB, True, Order1, Order2)
print(b)
WorkingMovingGoose.Runtime(player, position, OrderA, OrderB, False, Order1, Order2)

# ---------------------------------------------------------------------------------------------------------

# [KY] initialize variables required for order_match and fail check to work
# [KY] once player presses "done" on the machine, end stopwatch that begins when player accepts order and store time_taken as a variable

# Order_Match must be able to access the below variables somehow as they are used in the point system

wait_time = Order_Match_Function.waittime #placeholder, customer wait time (doesn't exist yet)
time_taken = Order_Match_Function.timetaken #placeholder, time elapsed from accepting an order to finishing the order here (doesn't exist yet)

# [KY] the below variables are adjusted by order_match until the game ends
# they must be initialized in main so that their values both start at 0
# initializing them in main also allows them to be easily accessed at the end of the game
# initializing them before the loop allows their values to accumulate as the order_match function is repeated

accuracies_below_30 = 0
total_points = 0

# ---------------------------------------------------------------------------------------------------------
#[KY] Initialize loop that runs an order and call functions
while True 

# [KY] Get value returned by Customer Order function in WorkingMovingGoose (since WorkingMovingGoose calls it first)
         orderchem = WorkingMovingGoose.Order
         
         
# [KY] Call Mixing function (confirm inputs)
         output = Mixing_Function.Mixing(mix1,mix2,mix3)
         #call function properly here

# [KY] Call Order Match and accuracy functions once done button is pressed
# Assign value returned by Order Match to points_per_order
         points_per_order = Order_Match_Function.order_match(output, orderchem)
         # [KY] output and orderchem are the variables assigned to the variables returned by 
         # Mixing Function and CustomerOrders, respectively
         # confirm function call

         accuracy = Order_Match_Function.accuracy_as_percent(output, orderchem)
         if accuracy < 30:
                  accuracies_below_30 += 1
                  #display 'X' to indicate that the player has less strikes left

# [KY] Add points earned from current order to total points
         total_points += points_per_order

def playAgain():
         #add graphics
         
# ---------------------------------------------------------------------------------------------------------

# [KY] game ends if accuracy (for amount produced) is below 30 for three non-consecutive orders or if time taken to complete order is greater than or equal to customer wait time
# 2 fail checks are implemented in case one of the checks does take forever to reach
# 30 can be adjusted once we test our game, not crucial to have a reasonable number for our game to work
# accuracies_below_30 is initialized by main

         #FIX GRAPHICS
         if accuracies_below_30 < 3 or time_taken < wait_time:
                  #display total_points and message for the player here
                  #end game here (break)
                  #allow player to play again?
                  
                  # [KY] display total points (check this is correct)
                  screen.fill((0,0,0))
                  font2 = pygame.freetype.SysFont(None, 36)
                  font.render_to(screen, (1010, 760), "Total points = " + str(total_points), (225, 255, 255))
                  
                  # [KY] use PlayerFail condition if we want to allow the player to play again 
                  # (not totally sure if this is the best way to do it)
                  PlayerFail = False
                  #repeat code for another order
                  #decrease timer value
                  #display strikes

         else:
                  # [KY] display points earned for the order (check this is correct)
                  screen.fill((0,0,0))
                  screen.blit("GAME OVER: Total points = " + str(total_points))
                  PlayerFail = True

if PlayerFail:
         if playAgain():
                  #allow player to play again
                  #reset values to 0 
                  accuracies_below_30 = 0
                  total_points = 0
         else:
                  break
         
         

                  


         



