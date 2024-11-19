
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

# Author: Nicholas Pribytkov ==================================================

# IMPORT PY FILES =============================================================

import WorkingMovingGoose # [NP] WorkingMovingGoose outputs visuals of the Customers and Orders.
#import TheMachine # [NP] TheMachine outputs visuals of the Machine at work, allowing the player to interface with it in order to mix chemicals together.

player, position, OrderA, OrderB, Order1, Order2 = WorkingMovingGoose.Customer()
b = WorkingMovingGoose.Runtime(player, position, OrderA, OrderB, True, Order1, Order2)
print(b)
WorkingMovingGoose.Runtime(player, position, OrderA, OrderB, False, Order1, Order2)

#Katie's stuff
#run order_match
order_match(orderchem, producedchem)
#end stopwatch here
if accuracy < 10
gameisDone = True
#do three strikes
