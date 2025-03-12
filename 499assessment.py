# imagine we have a genome 1mil bp long, sequencing reads are 100 bp long, how many reads do we need?
# for 1x read, 10000 reads end-to-end (goes thru exactly once)
# task: do multiple reads such as 5x, it goes thru the genome 5 times; how much of the genome has not been read

# breakdown 100 bp genome w 10 bp reads only needs 10 reads to read whole genome

import sys
import random
import math

trials = 100
genome_length = 1000000
reads = 50000
read_length = 100
bp_genome = [0] * genome_length # empty genome with given length

for i in range(reads): # amount of reads
    start_pos = random.randint(0, genome_length - read_length) # assign random read position
    for j in range(read_length): # for each read
        bp_genome[j + start_pos] +=1 

#print(bp_genome)
unread_bps = bp_genome[read_length : -read_length].count(0)
print(unread_bps)
print (1- (unread_bps/genome_length))
print(1 - math.e ** -5)