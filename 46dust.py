import sys
import math
import mcb185

# function for shannon entropy formula measures complexity of seq: find freq of each nt at each position, multiply the prob of each nt by log and find sum (neg)
def calc_entropy(seq):
    basecounter = {'A':0, 'C':0, 'G':0, 'T':0} # freq of nt at each position
    for base in seq:
        if base in basecounter:
            basecounter[base] += 1
    total = len(seq)
    entropy = 0.0
    for count in basecounter.values(): # for each nt
        if count > 0:
            p = count/total
            entropy -= p * math.log2(p) # multiply prob of nt by log and sum (neg)
    return entropy

# function for masking low complexity regions
def masklow(seq, w, entropy_thresh): # sequence, window size, entropy threshold
    seq_len = len(seq)
    masked_seq = list(seq) # converts seq to a list for mutability

    # sliding window
    for i in range(seq_len - w + 1):
        window = seq[i:i+w] # looks at just the window
        entropy = calc_entropy(window) # calc complexity of window
        if entropy < entropy_thresh: 
            masked_seq[i:i+w] = ['N'] * w # replace window with N to mask low complexity
    return ''.join(masked_seq) # convert list back to string and return

# main function to mask low complexity regions in given multi-fasta file
file_path = sys.argv[1]
window_size = int(sys.argv[2])
entropy_thresh = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(sys.argv[1]): # pulls data from input file
    masked_seq = masklow(seq, window_size, entropy_thresh)
    print(f">{defline}")
    print(masked_seq)