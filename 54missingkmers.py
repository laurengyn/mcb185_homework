import sys
import mcb185

def generate_kmers(k): # generate all kmers of k length
    bases = 'ACGT'
    kmers = [''] # empty string
    for i in range(k): # for the amount of possible positions
        kmerlist = [] # empty list for kmers
        for kmer in kmers: # for all kmer in string
            for base in bases: # for each base
                kmerlist.append(kmer + base) # add base to kmer
        kmers = kmerlist
    return kmers

def missing_kmers(seq): # find all missing kmers
    k = 1 # smallest possible kmer
    while True: # loop until we find a length w missing kmers
        seen = set() # kmers seen in seq
        for i in range(len(seq) - k + 1): # forward window
            kmer = seq[i:i +k]
            seen.add(kmer)

        rev_comp = mcb185.anti_seq(seq)
        for i in range(len(rev_comp) - k + 1): # reverse comp window
            kmer = rev_comp[i:i + k]
            seen.add(kmer)
        
        all_possible_kmers = set(generate_kmers(k)) # find all kmers of k length
        missing = all_possible_kmers - seen # subtract all kmers from kmers seen to find missing kmers
        if missing:
            print(f"smallest missing kmers at k={k}:")  # lists all missing kmers
            for m in sorted(missing): print(m)
            print(f"total missing kmers at k={k}: {len(missing)}") # tells us number of missing kmers
            break
        k += 1

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    missing_kmers(seq)