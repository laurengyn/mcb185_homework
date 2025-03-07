import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10 # window
for i in range(len(seq) -w +1): # +1 accounts for start at 0
    s = seq[i:i+w] # sequence from start to 10 nts after
    print(i, sequence.gc_comp(s), sequence.gc_skew(s)) # print window index and GC content and skew