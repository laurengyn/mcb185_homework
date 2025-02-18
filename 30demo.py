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

tax = ('Homo', 'sapiens', 9606)  # construct tuple
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
nts[2] = 'G'
print(nts)