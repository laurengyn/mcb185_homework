import sys
import mcb185
import math

'''
Write a program that performs a statistical summary of the lengths of sequences in a FASTA file. 
It should report: count, min, max, mean, stdev, median, and N50. 
Use it on the file of E. coli proteins.
'''
lengths = [] # empty list for the length of sequences

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    seq = defwords[4]
    lengths.append(len(seq))

lengths.sort()
count = len(lengths)

min = lengths[0]
max = lengths[0]
sum = 0
for val in lengths:
    if val < min: min = val
    if val > max: max = val
    sum += val

mean = sum / count

sdsum = 0
for val in lengths:
    sd = ((val - mean) ** 2)
    sdsum += sd
standev = math.sqrt(sdsum / (count - 1))

if count % 2 == 1: median = lengths[count // 2]
else: median = (lengths[count // 2 - 1] + lengths[count // 2])/2

lengths.sort(reverse=True)
nsum = 0
middle = sum/2
n50 = 0
for val in lengths:
    nsum += val
    if nsum < middle: n50 = nsum
    else: break

print(count, min, max, mean, standev, median, n50)