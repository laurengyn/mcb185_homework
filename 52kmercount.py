import sys
import mcb185

k = int(sys.argv[2]) # sets up command line parameter for value of k
kcount = {} # empty dictionary
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) -k +1): # window
        kmer = seq[i:i+k] # creates variable
        if kmer not in kcount: kcount[kmer] = 0 # sets count of kmer
        kcount[kmer] += 1 # increases count of kmer
for kmer, n in kcount.items(): print(kmer, n)


import itertools
for nts in itertools.product('ACGT', repeat=k):
    kmer = ''.join(nts) # joins tuple ns into string to index dictionary
    if kmer in kcount: print(kmer, kcount[kmer])
    else:              print(kmer, 0)