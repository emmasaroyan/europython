import random 

# Initialize 10 dice 
die_1 = random.randint(1,6)
die_2 = random.randint(1,6)
die_3 = random.randint(1,6)
die_4 = random.randint(1,6)
die_5 = random.randint(1,6)
die_6 = random.randint(1,6)
die_7 = random.randint(1,6)
die_8 = random.randint(1,6)
die_9 = random.randint(1,6)
die_10 = random.randint(1,6)

def take_turn(dice):
    """Calculate the player's total score"""
    total = 0
    for die in dice:
        if die > 1:
            total += die
        else: 
            total += 1
    return total 

take_turn([die_1, die_2])

