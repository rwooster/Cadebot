# Contains utility functions

import random

def roll_dice(dice):
    # Make a dice roll of the form "1d6" 

    roll = dice.split('d') 

    random.seed()
    total = 0
    for i in range(int(roll[0])):
        total += random.randint(1, int(roll[1]))
    return total
