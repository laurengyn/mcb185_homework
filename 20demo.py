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