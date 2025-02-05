import math

# Tuples
t = 1, 2
print (t)
print (type(t))

person = 'Steve', 21, 57891.50
print (person)
print (type(person))

def midpoint (x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
print (midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print (my, mx)
print (m[0], m[1])

# Iteration
## while loop
i = 0
while i < 3:
    i = i + 1
    print ('hey', i)

i = 0
while i < 10:
    print (i)
    i = i + 3
print ('final value of i is', i)


## for loop
for i in range (1, 10, 3): ### range (start, stop, step)
    print (i)
### technically, don't need step or start (it'll start at 0)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print (thing)

for i in range (len(basket)):
    print (basket[i])


## nesting loops
for i in range (7):
    if i % 2 == 0: print (i, 'is even')
    else: print (i, 'is odd')

## PRACTICE PROBLEMS
'''
Write a function that calculates the triangular number. 
This is the sum of numbers from 1 to n.
'''
def triangular_num (n):
    sum = 0 
    for i in range (n): ## range ends just before n
        sum = sum + i + 1
    return sum

print (triangular_num(3)) ## should equal 6

'''
Write a function that calculates the factorial of a number.
'''
def factorial (n):
    prod = 1
    for i in range (2, n + 1):
        prod = prod * i
    return prod

print (factorial(5)) ## should equal 120

'''
Write a function that computes the Poisson probability 
of k events occurring with an expectation of n: n^k e^-n / k!
'''
def poisson (n, k):
    return (n ** k) * (math.e ** -n) / factorial(k)

print (poisson(2, 3)) ## should equal 0.18044704431548356

'''
Write a function that solves "n choose k": n! / k!(n - k)!
'''
def nchoosek (n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print (nchoosek(5, 2)) ## should equal 10

'''
Write a function that estimates Euler's number: 
e (2.71828...). This can be computed as the infinite sum of 1/n!. 
Choose a finite number of iterations.

note to self: check w ta if this is the correct interpretation of the problem
'''

def euler (n):
    sum = 0
    for i in range (n + 1):
        sum = sum + 1 / factorial (i)
    return sum

print (euler(10)) ## should equal 2.7182815255731922

'''
Write a function to determine if a number is prime.
'''

def is_prime (n):
    for i in range (2, n): 
        if n % i == 0: return False
    return True

print (is_prime(7)) ## should return True
print (is_prime(8)) ## should return False

'''
Write a function that estimates Pi using the Nilakantha series. 
Again, choose a finite limit.

STUDY THIS!!!
'''

def calc_pi(n):
    pi = 3
    for i in range(1, n+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

print (calc_pi(10)) ## should equal 3.141592653589793

# Random Numbers
import random

for i in range(5):
    print(random.random())

for i in range(3):
    print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2) ## resets seed
print(random.random())
print(random.random())
random.seed(1) ## notice how they are the same as the first two randoms
print(random.random())
print(random.random())

# Compound Assignment
i = 0
while i < 10:
    print (i)
    i = i + 3
print ('final value of i is', i)

i = 0
while i < 10:
    print (i)
    i += 3
print ('final value of i is', i)

## PRACTICE PROBLEMS
'''
Write a program that estimates pi using Monte Carlo methods. 
Generate random values for x and y from 0 to 1. 
Calculate the distance to the origin. 
If the distance is less than 1, the point is inside the circle. 
The ratio of points that fall inside compared to the total is pi/4. 
Output each iteration and watch as the ratio gets closer to pi. 
Use an endless while loop in your program and stop it with ^C.
'''

def estimate_pi ():
    ratio_inside = 0
    i = 0
    while True:
        x = random.random()
        y = random.random()
        i += 1
        if (x ** 2 + y ** 2) < 1: 
            ratio_inside += 1
        print (ratio_inside / (i + 1) * 4)

### estimate_pi() ## uncomment to run

'''
In Dungeons and Dragons, each character is described by 6 statistics (strength, intelligence, wisdom, dexterity, constitution, charisma). 
In the old days, each stat was decided by summing up the values on 3 six-sided dice (3D6). 
Each stat therefore has a range of 3-18 and an average of 10.5. 
Over the years, the official rules have changed and many players have added their own house rules. 
Write a program that determines the average stat value using the various rules below.
    - 3D6: roll 3 six-sided dice
    - 3D6r1: roll 3 six-sided dice, but re-roll any 1s
    - 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
    - 4D6d1: roll 4 six-sided dice, dropping the lowest die roll
'''

def avg_three_d_six ():
    sum = 0
    count = 0
    while count <3:
        roll = random.randint(1, 6)
        print (roll)
        sum += roll
        count += 1
    return (sum/3)

print (avg_three_d_six())
print (avg_three_d_six())
print (avg_three_d_six()) ## did three to make sure it was random


def avg_three_d_six_r_one ():
    sum = 0
    count = 0
    while count <3:
        roll = random.randint(1, 6)
        print (roll)
        if roll > 1:
            sum += roll
            count += 1
    return (sum/3)

print (avg_three_d_six_r_one())
print (avg_three_d_six_r_one())
print (avg_three_d_six_r_one()) ## did three to make sure it was random

def avg_three_d_six_x_two ():
    sum = 0
    count = 0
    while count <3:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print (roll1, roll2)
        if roll1 > roll2:
            sum += roll1
            print ('higher is', roll1)
        else:
            sum += roll2
            print ('higher is', roll2)
        count += 1
    return (sum/3)

print (avg_three_d_six_x_two())
print (avg_three_d_six_x_two())
print (avg_three_d_six_x_two()) ## did three to make sure it was random

def avg_four_d_six_d_one ():
    sum = 0
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    roll4 = random.randint(1, 6)
    print (roll1, roll2, roll3, roll4)
    if roll1 <= roll2 and roll1 <= roll3 and roll1 <= roll4:
        sum += roll2 + roll3 + roll4
    elif roll2 <= roll1 and roll2 <= roll3 and roll2 <= roll4:
        sum += roll1 + roll3 + roll4
    elif roll3 <= roll1 and roll3 <= roll2 and roll3 <= roll4:
        sum += roll1 + roll2 + roll4
    else:
        sum += roll1 + roll2 + roll3
    return (sum/3)
 
print (avg_four_d_six_d_one())
print (avg_four_d_six_d_one())
print (avg_four_d_six_d_one()) ## did three to make sure it was random

# ASSESSMENT EXAMPLE
'''
Write a program that that estimates pi using the Gregory-Leibniz series. 
pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 .... 
Make the program run endlessly.
'''

CODE HERE

'''
Halflings get advantage on death saves. 
Modify your program to determine the halfling rate for death, stable, and revive.
'''

CODE HERE