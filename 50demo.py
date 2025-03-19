## SETS
s = {'A', 'C', 'G'} # curly brackets = set, indicate unordered
print (s)

s.add('T')
print(s)

s.add('A')
print(s)

# print(s[2]) # creates error bc unordered set


## DICTIONARY
d = {} # create empty dictionary
d = dict() # same as prev

d = {'dog': 'woof', 'cat': 'meow'} # indices of dictionaries are strings not numbers
print(d)

print(d['cat']) # retrieves definition

d['pig'] = 'oink' # add new item to dictionary
print(d)

d['cat'] = 'mew' # change value of item
print(d)

del d['cat'] # delete an item
print(d)

# print(d['rat']) # creates error bc key doesn't exist

if 'dog' in d: print(d['dog']) # instead, check for key first

### ITERATION
for key in d: print(f'{key} says {d[key]}') # iterates over keys in chronological order

for k, v in d.items(): print(k, 'says', v) # d.items() is a iteration tool

for thing in d.items(): print(thing[0], thing[1]) # BAD DON'T DO

print(d.keys(), d.values(), list(d.values())) # use dict.keys() or dict.values() to select keys/values and list(dict.values/keys()) for lists


## LOOKUP TABLES: best way to lookup values from a table
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)

import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)