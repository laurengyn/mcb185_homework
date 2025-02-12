'''
Death saves are a little different than normal saving throws. 
If your health drops to 0 or below, you are unconscious and may die. 
Each time it is your turn, roll a d20 to determine if you get closer 
to life or fall deeper into death. If the number is less than 10, you record a "failure". 
If the number is 10 or greater, you record a "success". 
If you collect 3 failures, you "die". If you collect 3 successes, you are "stable" but unconscious. 
If you are unlucky and roll a 1, it counts as 2 failures. 
If you're lucky and roll a 20, you gain 1 health and have "revived". 
Write a program that simulates death saves. What is the probability one dies, stabilizes, or revives?
'''

import random
import math

'''
def death_saves():
    success = 0
    fail = 0
    while success < 3 and fail < 3:
        roll = random.randint(1, 20)
        print (roll)
        if roll == 1:
            fail += 2
            print ('Failed twice, fail count', fail)
        elif roll == 20:
            success = 3
            print ("You have revived")
        elif roll < 10:
            fail += 1
            print ('Fail count', fail)
        elif roll >= 10:
            success += 1
            print ('Success count', success)
            if success == 3:
                print ("You are stable but unconscious")
        else:
            print ("Neither success nor fail")
    if fail == 3:
        print ("You die")

death_saves()
'''

def death_saves_prob():
    revive = 0
    stabilize = 0
    die = 0
    trials = 0
    while True:
        trials += 1
        success = 0
        fail = 0
        while success < 3 and fail < 3:
            roll = random.randint(1, 20)
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

death_saves_prob()