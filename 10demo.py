# 10.py by lauren nguyen

import math

print ("hello, again") #greeting

print (1.5e-2) #sample numbers

## sample math operators
print (1 + 1) #add
print (1 - 1) #subtract
print (2 * 2) #multiply
print (1 / 2) #divide
print (2 ** 3) #exponent
print (5 // 2) #integer divide
print (5 % 2) #remainder
print (5 * (2 + 1)) #precedence


## sample math functions
print (abs (1)) #absolute value
print (abs (-1)) 
print (pow (2,3)) #powers
print (round (3.14159, ndigits=4)) #round
print (math.ceil(3.5)) #round up
print (math.floor(3.5)) #round down


## numbers aren't real
print (0.1 * 1)
print (0.1 * 3)


## variable assignment
a = 3 # side of triangle
b = 4 # other side of triangle
c = math.sqrt (a**2 + b**2) # equation for hypotenuse
print(c)
print (type(a), type(b), type(c)) #to see the type of variable
print(type(a), type(b), type(c), sep=', ', end='!\n') # adds separators and ends


## functions
def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

def pythagoras(a, b): return math.sqrt(a**2 + b**2)

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h

def triangle_area(w, h): return rectangle_area(w, h) / 2

s = 'hello world'
print(s, type(s))


## conditionals
a = 2
b = 2
if a == b:
    print('a equals b')
    print (a, b)
print (a, b)

def is_even(x):
    if x % 2 == 0: return True
    return False
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if  a < b: print('a < b')
elif a > b: print('a > b')
else:   print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')


## none type
def silly(m, x, b):
    y = m * x + b
print(silly(2, 3, 4))

