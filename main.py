
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

# Welcome to Goose _____ (name still in progress). You are asked to work at a
# chemical facility, where you talk to customers who wish to buy chemicals,
# track their orders, mix chemicals up and give them the chemicals they want!
# 
# Work carefully but vigilantly to give customers their desired chemicals and
# recieve $$$$$ the bag $$$$$$.


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

[KY] #initialize variables required for order_match to work
[KY] #once player presses "done" on the machine, end stopwatch that begins when player accepts order and store time_taken as a variable

wait_time = #placeholder, store timer value here
time_taken = #placeholder, store time elapsed from accepting an order to finishing the order here
time_difference = wait_time - time_taken
accuracies_below_30 = 0

---------------------------------------------------------------------------------------------------------

# [KY] Check to see if game has ended (put in its own file?)
# [KY] Refer to order match function to see how the below variables are defined
if accuracy_percent < 30 or chem_match == False:
         accuracies_below_30 += 1

if accuracies_below_30 == 3 or time_taken >= wait_time:
         #end game here (break)

else:
         #repeat code for another order



