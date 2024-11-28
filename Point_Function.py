# POINT FUNCTION ==============================================================

# This file determines the point payout of the fulfilment of the order 
# depending on various factors like accuracy, difficulty and time.

# Parent: GooseUpdates ================================================================
# Author: Katie Yu ============================================================
# Editor(s): Nicholas Pribytkov ===============================================

def point_calculation(Difficulty, accuracy_fraction, time_fraction):
    
    points_per_order = int((Difficulty + time_fraction)*accuracy_fraction))
    # [KY] Sample points_per_order = ((20 + ((20-10)/20))*0.8) = 16

    # [KY] time_fraction is (time given - time taken)/(time given)

    return points_per_order
