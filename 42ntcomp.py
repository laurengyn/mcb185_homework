## cut out parts to see how different methods work
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split() # sequence name
    name = defwords[0]
      
    ## METHOD ONE: counts G and C nucelotides
    gc = 0
    for nt in seq:
        if nt == 'C' or nt == 'G': gc += 1
    print(name, gc/len(seq)) # prints name and GC fraction
    
    ## METHOD TWO: INDIVIDUAL VARIABLES, counts each nucleotide separately
    A = 0
    C = 0
    G = 0
    T = 0
    N = 0
    for nt in seq:
        if nt == 'A': A += 1
        elif nt == 'C': C +=1
        elif nt == 'G': G +=1
        elif nt == 'T': T +=1
        else: N += 1
    print (name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
    
    ## METHOD THREE: LIST VARIATION, puts the counts in a list
    counts = [0, 0, 0, 0, 0] # one for each nucleotide
    for nt in seq:
        if nt == 'A': counts[0] += 1
        elif nt == 'C': counts[1] += 1
        elif nt == 'G': counts[2] += 1
        elif nt == 'T': counts[3] += 1
        else: counts[4] += 1
    print(name, end=' ')
    for n in counts: print(n/len(seq), end=' ')
    print()
    
    ## METHOD FOUR: INDEXING WITH STR.FIND(), streamlines method three by finding the char position in string given 
    nts = 'ACGTN'
    counts = [0] * len(nts) # creates list no matter how many nucleotides
    for nt in seq:
        idx = nts.find(nt)
        counts[idx] += 1
    print(name, end=' ')
    for n in counts: print(n/len(seq), end= ' ')
    print()
    
    ## METHOD FIVE: COUNTING ANY LETTER, makes lists within code, prints a table
    nts = []
    counts = []
    for nt in seq:
        if nt not in nts: # adds new nucleotides
            nts.append(nt)
            counts.append(0)
        idx = nts.index(nt)
        counts[idx] += 1
    print(name)
    for nt, n in zip(nts, counts): # loops thru nts and counts list together
        print(nt, n, n/len(seq)) # prints letter, count, frequency
    print()
    
    ## METHOD  SIX: COUNTING WITH STR.COUNT(), counts specific nucleotides in each iteration
    print(name, end=' ')
    for nt in 'ACGTN':
        print(seq.count(nt) / len(seq), end=' ')
    print()