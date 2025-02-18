import random
import math
'''
def death_saves_prob_adv():
    revive = 0
    stabilize = 0
    die = 0
    trials = 0
    while True:
        trials += 1
        success = 0
        fail = 0
        while success < 3 and fail < 3:
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 20)
            if roll1 >= roll2: roll = roll1
            if roll2 >= roll1: roll = roll2

            if roll == 1:
                fail += 2
            if roll == 20:
                success = 3
                revive += 1
            elif roll < 10:
                fail += 1
            elif roll >= 10:
                success += 1
                if success == 3:
                    stabilize += 1
            if fail >= 3:
                    die += 1
        print (revive/trials, stabilize/trials, die/trials)

death_saves_prob_adv()
'''
multiplier = 1
denominator = 1
sum = 0
while True: 
    sum = sum + multiplier*(1/denominator)
    multiplier *= -1
    denominator += 2
    print (sum*4)