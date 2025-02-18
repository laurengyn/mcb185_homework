import math

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper()) ## all uppercase
print(s)

print(s.replace('o', '')) ## removes all o's
print(s.replace('o', '').replace('r', 'i')) ## removes all o's, replaces r's with i's


print('STRING FORMATTING')

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":>30}')
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify
print(f'{20:<20} {10}') 
print(f'{"hello world":^20}')    # center justify
print(f'{"hello world":^30}')
print(f'{"hello world":>20} {"hello world":^20} {"hello world":<20}')

print('{} {:.3f}'.format('str.format', math.pi)) # rounds to 3 decimal points
print('{} {:.5f}'.format('str.format', math.pi)) # rounds to 5 decimal points

print('%s %.3f' % ('printf', math.pi))
print('%s %.5f' % ('printf', math.pi))


print('INDEXES')

seq = 'GAATTC'
print(seq[0], seq[1]) ## prints first and second char of sequence
print(seq[-1]) ## prints first char from the right

for nt in seq:
    print(nt, end='') # prints all in one line/string
print()

for nt in seq:
    print(nt) # prints one nucleotide per line
print()

for nt in seq:
    print(nt, end='!') # prints all in one line with ! after each letter
print()

for nt in seq:
    print(nt, end=' ') # prints all in one line with space after each letter
print()

for i in range(len(seq)): # len means length
    print(i, seq[i])

for i in range(len(seq)): # starts at 1 instead of 0
    print(i+1, seq[i])


print('SLICES')

s = 'ABCDEFGHIJ'
print(s[0:5]) # prints first character to the character before the sixth
print(s[0:8:2]) # step size again!

print(s[0:5], s[:5])        # both ABCDE; assumes the initial value
print(s[5:len(s)], s[5:])   # both FGHIJ; assumes the final value

print(s, s[::], s[::1], s[::-1]) # last one has negative step so starts at the end?
print(s[9::-1]) # prints same thing as fourth of previous command

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3): # in the string, from first to last char every third char
    codon = dna[i:i+3] # prints current char plus two following chars
    print(i, codon) # adds number to it


print('TUPLES')

tax = ('Homo', 'sapiens', 9606)  # construct tuple, can't change contents
print(tax)                       # note the parentheses in the output

print(tax[0])      # index
print(tax[::-1])   # slice


print('ENUMERATE & ZIP')

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

for i, nt in enumerate(nts): # enumerate is same as range + len
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

for nt, name in zip(nts, names):
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)


print('LISTS')

nts = ['A', 'T', 'C']
print(nts)

nts[2] = 'G' # can change contents of lists
print(nts)

nts.append('C') # add to list
print(nts)

last = nts.pop()  # removes last item of list
print(last)

nts.sort() # sorts alphabetically
print(nts)

nts.sort(reverse=True) # sorts reverse alphabetical
print(nts)

nucleotides = nts # means both are the same list, not a copy
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

nts.copy() 
# ASK TA

items = list() # creates empty list
print(items)
items.append('eggs')
print(items)

stuff = [] # also a way to create an empty list
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph) # makes string into list
print(aas)

text = 'good day          to you'
words = text.split() # splits strings by words (through spaces)
print(words)

line = '1.41,2.72,3.14'
print(line.split(',')) # splits by comma

s = '-'.join(aas) # consolidates lists into strings with dash between
print(s)
s = ''.join(aas) # consolidates lists into strings
print(s)


print('SEARCHING') # can use in, find(), and index()

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z')) # gives error bc not found

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z')) # gives -1 bc it cannot be found;


print('PRACTICE PROBLEMS')

# Write a function that returns the minimum value of a list.
def minimum(lista):
    lowest = lista[0]
    for i in lista[1:len(lista)]:
        if i < lowest: 
            lowest = i
    return lowest

listtest = [42, 14, 30]
print(minimum(listtest))

# Write a function that returns both the minimum and maximum values of a list.
def min_and_max(lista):
    lowest = lista[0]
    highest = lista[0]
    for i in lista[1:len(lista)]:
        if i < lowest: 
            lowest = i
        if i > highest:
            highest = i
    return lowest, highest

print(min_and_max(listtest))

# Write a function that returns the mean of the values in a list.
def mean(lista):
    sum = 0
    for i in lista:
        sum += i
    return (sum/len(lista))

print(mean(listtest))

# Write a function that computes the entropy of a probability distribution. 
def entropy(lista):
    sum = 0
    for i in lista:
        if i >= 0 and i <= 1.0:
            compute = i * math.log2(i)
            sum -= compute
    return sum

print(entropy([0.4, 0.88, 0.21]))

# Write a function that computes the Kullback-Leibler distance between two sets of probability distributions.
def kl_dist(lista, listb):
    sum = 0
    for a, b in zip(lista, listb):
        compute = a * math.log2(a/b)
        sum += compute
    return sum


print('COMMAND LINE DATA')

import sys
print(sys.argv) # ASK TA

i = int('42') # converts number string to true integer
x = float('0.61803') # converts number string to true float
print(i * x)

# x = float('hello') ## results in error bc it's not a number


print('PAIRWISE COMPARISON')
'''
for i in range(0, len(list)):
    for j in range(0, len(list)): 
        print(j)
'''
## X = 0, all combo
## X = i, half-matrix w diagonal
## X = i+1, half matrix w/o diagonal 