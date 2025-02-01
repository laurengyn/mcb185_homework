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