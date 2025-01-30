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

# Practice
print ("PRACTICE")

### Convert temperature from F to C or vice-versa
def farenheit_to_celcius(num): return (num - 32) * (5/9)
def celcius_to_farenheit(num): return (num * (9/5)) + 32

print (farenheit_to_celcius(32))
print (celcius_to_farenheit(0))

### Convert speed from MPH to KPH or vice-versa
def mph_to_kph(num): return num * 1.60934
def kph_to_mph(num): return num / 1.60934

print (mph_to_kph(60))
print (kph_to_mph(100))

### Compute DNA concentration from OD260
def dna_concentration(num): return num * 50

print (dna_concentration(0.1))

### Compute the arithmetic mean of 3 numbers
def arith_mean(a, b, c): return (a + b + c) / 3

print (arith_mean(1, 2, 3))

### Compute the geometric mean of 3 numbers
def geo_mean(a, b, c): return (a * b * c) ** (1/3)

print (geo_mean(1, 2, 3))

### Compute the harmonic mean of 3 numbers
def harm_mean(a, b, c): return 3 / ((1/a) + (1/b) + (1/c))

print (harm_mean(1, 2, 3))

### Compute the distance between 2 points in a graph
def dist_points(x1, y1, x2, y2): return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print (dist_points(1, 2, 3, 4))


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

# Practice
print ("PRACTICE")
### Write a function that determines if a number is an integer. 
### A good name for such a function would be is_integer() or isinteger(). 
### Functions with Boolean return values often have is in their prefix. 
### To solve this problem, try using // or %.
def is_integer(a): 
    if a == a // 1: return True
    else: return False

print (is_integer(1.0))
print (is_integer(1.5))

### Write a function that determines if a number is a valid probability.
def is_valid_prob(a):
    if a <= 1 and a >=0: return True
    else: return False

print (is_valid_prob(0.5))
print (is_valid_prob(1.5))
print (is_valid_prob(-0.5))

### Write a function that returns the molecular weight of a DNA letter. 
### If the letter doesn't match any nucleotide, return None.
def dna_weight(a):
    if a == 'A': return 313.21
    elif a == 'T': return 304.2
    elif a == 'C': return 289.18
    elif a == 'G': return 329.21
    else: return None

print (dna_weight('A'))
print (dna_weight('T'))
print (dna_weight('C'))
print (dna_weight('G'))
print (dna_weight('U'))

### Write a function that returns the complement of a DNA letter, returning None if the letter isn't DNA.
def dna_complement(a):
    if a == 'A': return 'T'
    elif a == 'T': return 'A'
    elif a == 'C': return 'G'
    elif a == 'G': return 'C'
    else: return None 

print (dna_complement('A'))
print (dna_complement('T'))
print (dna_complement('C'))
print (dna_complement('G'))
print (dna_complement('U'))

#Assessment Example
print ("ASSESSMENT EXAMPLE")
### Write a function that computes the distance between 2 points in a graph.
def dist_points(x1, y1, x2, y2): return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print (dist_points(1, 2, 3, 4))

### Write a function that returns the complement of a DNA letter, returning None if the letter isn't DNA.
def dna_complement(a):
    if a == 'A': return 'T'
    elif a == 'T': return 'A'
    elif a == 'C': return 'G'
    elif a == 'G': return 'C'
    else: return None 

print (dna_complement('A'))
print (dna_complement('T'))
print (dna_complement('C'))
print (dna_complement('G'))
print (dna_complement('U'))

### Write a function max3() that returns the maximum of 3 numbers.
def max3(a, b, c):
    if a >= b and a >= c: return a
    elif b >= a and b >= c: return b
    else: return c

print (max3(1, 2, 3))

### Why do you think PHRED quality values are -10 * log10 rather than -log2? 
### How would you modify your program if you thought log2 was better?
def char_to_prob(a):
    if ord(a) >= 32 and ord(a) <= 126:
        return (2 ** (-(ord(a) - 33)))
    return None


def prob_to_char(num):
    if num <= 1 and num > 0: 
        ascii_value = round ((math.log2(num)) + 33)
        if  ascii_value >= 32 and ascii_value <= 126:
            return chr (ascii_value) 
    return None