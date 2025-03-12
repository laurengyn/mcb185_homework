import sys
import mcb185
import sequence
'''
def get_protein(seq, t): # where seq is seq of nts and t is the minimum number of aas
    proteins = []
    for i in range (3): # checks all reading frame possibilities
        translation = mcb185.translate(seq[i:]) # fully translates seq into aa chain
        orfs = translation.split('*') # splits the aa chain by stop codons
        for orf in orfs:
            if 'M' not  in orf: continue # skip any chains without start codon
            idx = orf.index('M') # finds first M unit 4!
            pro = orf[idx:] # finds whole chain starting at M
            if len(pro) >= t: proteins.append(pro) # stores valid proteins
    return proteins

min_length = int(sys.argv[2]) # pulls the minimum length of aa chain

for defline, seq in mcb185.read_fasta(sys.argv[1]): # pulls data from input file
    defwords = defline.split()
    name = defwords[0]
    p = 0
    for protein in get_protein(seq, min_length):
        print(f'>{name}-prot-{p}') # prints name
        print (protein) # prints valid strand
        p += 1
'''



# CODERIE RANDOM TASK: apparently 950
import random
'''
def dna_random(length): 
    return ''.join(random.choices('ACGT', k=length))
'''
dna_random = ''.join(random.choices('ACGT', k=4600000))

def find_proteins(seq, t): # where t is the minimum number of aas
    proteins = 0
    for i in range (3): # checks all reading frame possibilities
        translation = mcb185.translate(seq[i:]) # fully translates seq into aa chain
        orfs = translation.split('*') # splits the aa chain by stop codons
        for orf in orfs:
            if 'M' not  in orf: continue # skip any chains without start codon
            idx = orf.index('M') # finds first M
            pro = orf[idx:] # finds whole chain starting at M
            if len(pro) >= t: proteins += 1 # adds valid protein to count
    return (2*proteins) # returns total valid proteins found in nts seq

print(find_proteins(dna_random, 100))
