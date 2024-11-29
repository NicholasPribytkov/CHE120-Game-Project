# POINT FUNCTION ==============================================================

# This file determines the point payout of the fulfilment of the order 
# depending on various factors like accuracy, difficulty and time.

# Parent: GooseUpdates ================================================================
# Author: Katie Yu ============================================================
# Editor(s): Nicholas Pribytkov ===============================================

def point_calculation(Difficulty, accuracy_fraction, time_fraction):
    
    points_per_order = int((Difficulty)*(time_fraction)*(accuracy_fraction))

    # [KY] Difficulty of the order is theoretically the highest number of points you can earn per order
    # [KY] Sample points_per_order = ((20*((40-5)/40)*0.8) = 14
    # Medium difficulty, little time taken, high accuracy

    # [KY] Sample points_per_order = ((30*((50-40)/50)*0.6) = 4
    # High difficulty, large percentage of time taken, medium accuracy

    # [KY] time_fraction is (time given - time taken)/(time given), as defined in GooseUpdates.py (fraction of time remaining)

    return points_per_order
