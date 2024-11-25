# POINT FUNCTION ==============================================================

# This file determines the point payout of the fulfilment of the order 
# depending on various factors like accuracy, difficulty and time.

# Parent: GooseUpdates ================================================================
# Author: Katie Yu ============================================================
# Editor(s): Nicholas Pribytkov ===============================================

def point_calculation(Difficulty, accuracy_fraction, time_difference):
    
    points_per_order = int((Difficulty + time_difference)*(accuracy_fraction))
    # [KY] Sample points_per_order = (20 + (20-10))*0.8 = 24

    return points_per_order
