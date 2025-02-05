'''
One of the core mechanics of D&D is the "saving throw". 
When certain events happen, you need to roll a d20 to figure out if you succeed or not. 
For example, you are walking across a frozen lake and it begins to crack underfoot. 
If you make a saving throw, you step aside. If you fail, you fall in. 
Some saving throws are more difficult than others. 
If the ice is very thick, the "difficulty class" (DC) may be only 5. 
This means you only need to roll a 5 or higher to succeed. 
However, if the ice is thin and has a DC of 15, you will need a roll of 15 or higher to succeed. 
Certain events may give you "advantage" or "disadvantage". 
For example, if you have a rope tied around your waist and a friend is 
instructed to pull you aside if anything bad happens, you could have "advantage". 
This allows you to roll two d20s and take the larger value. 
You may also have disadvantage, for example another "friend" pushes 
you from behind, causing you to stumble forward. 
In this case, you have "disadvantage" and must take the lower of two d20 rolls.

Write a program that simulates saving throws against DCs of 5, 10, and 15.
'''

import random
import math

def saving_throws (n): 
    d20 = random.randint(1, 20)
    print(d20)
    if d20 >= n:
        print("You rolled higher than or equal to", n)
    else:
        print("You rolled lower than", n)

saving_throws(5)
saving_throws(5)
saving_throws(10)
saving_throws(10)
saving_throws(15)
saving_throws(15)

def saving_throws_advantage (n): 
    d20_1 = random.randint(1, 20)
    d20_2 = random.randint(1, 20)
    print (d20_1, d20_2)
    if d20_1 >= d20_2:
        print (d20_1)
    else:
        print (d20_2)
    if d20_1 >= n or d20_2 >= n:
        print ("You rolled higher than or equal to", n)
    else:
        print ("You rolled lower than", n)

saving_throws_advantage(5)
saving_throws_advantage(5)
saving_throws_advantage(10)
saving_throws_advantage(10)
saving_throws_advantage(15)
saving_throws_advantage(15)

def saving_throws_disadvantage (n):
    d20_1 = random.randint(1, 20)
    d20_2 = random.randint(1, 20)
    print(d20_1, d20_2)
    if d20_1 <= d20_2:
        print (d20_1)
        if d20_1 >= n:
            print ("You rolled higher than or equal to", n)
        else:
            print ("You rolled lower than", n)
    else:
        print (d20_2)
        if d20_2 >= n:
            print ("You rolled higher than or equal to", n)
        else:
            print ("You rolled lower than", n)

saving_throws_disadvantage(5)
saving_throws_disadvantage(5)
saving_throws_disadvantage(10)
saving_throws_disadvantage(10)
saving_throws_disadvantage(15)
saving_throws_disadvantage(15)