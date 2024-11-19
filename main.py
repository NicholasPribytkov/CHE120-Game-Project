
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

# Welcome to Goose Lab. You are asked to work at a
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

import WorkingMovingGoose # [NP] WorkingMovingGoose outputs visuals of the Customers and Orders.
#import TheMachine # [NP] TheMachine outputs visuals of the Machine at work, allowing the player to interface with it in order to mix chemicals together.

player, position, OrderA, OrderB, Order1, Order2 = WorkingMovingGoose.Customer()
b = WorkingMovingGoose.Runtime(player, position, OrderA, OrderB, True, Order1, Order2)
print(b)
WorkingMovingGoose.Runtime(player, position, OrderA, OrderB, False, Order1, Order2)

---------------------------------------------------------------------------------------------------------
#Priority 2
[KY] #initialize variables required for order_match and fail check to work (these can go in the order match function right)
[KY] #once player presses "done" on the machine, end stopwatch that begins when player accepts order and store time_taken as a variable

wait_time = #placeholder, store timer value here (@ppl working on timers)
time_taken = #placeholder, store time elapsed from accepting an order to finishing the order here

#[KY] the below variables are adjusted by order_match as the game progresses
accuracies_below_30 = 0
total_points = 0
---------------------------------------------------------------------------------------------------------
#Priority 1
# [KY] Check to see if game has ended (fail check)
# [KY] Refer to order match function to see how the below variables are defined

if accuracy_percent < 30 or chem_match == False:
         accuracies_below_30 += 1
         #display 'X' to indicate that the player has less strikes left

# [KY] game ends if accuracy (for amount produced) is below 30 for three non-consecutive orders or if time taken to complete order is greater than or equal to customer wait time
# 30 can be adjusted once we test our game, not crucial for our game to end within a reasonable amount of time
# accuracies_below_30 is initialized by order match

if accuracies_below_30 == 3 or time_taken >= wait_time:
         #display (total_points) and message for the player
         #end game here (break)

else:
         #repeat code for another order
         #decrease timer value
         #how easy is it to get correct accuracy
         #display strikes



