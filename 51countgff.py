import sys
import gzip

count = {} # empty dictionary
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line.startswith('#'): continue # another useful function is str.endswith()
        f = line.split() # retrieve feature name from line
        feature = f[2]
        if feature not in count: count[feature] = 0 # if feature is not in dictionary, create key
        count[feature] += 1 # counting
for f, n in count.items(): print(f, n) # reports count of each feature

'''
ALT LINES 7 & 8
        if feature not in count: count[feature] = 1
        else:                    count[feature] += 1
'''

## composition counting letters
count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1

## sorting
for k in sorted(count): print(k, count[k]) # sorts by keys

for k, v in sorted(count.items(), key=lambda item: item[1]): # sort by values, reads tuple 'item' and returns second item (item[1])
    print(k, v)

def by_value(tuple):
    return tuple[1]

for k, v in sorted(count.items(), key=by_value):
    print(k, v)