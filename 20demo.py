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