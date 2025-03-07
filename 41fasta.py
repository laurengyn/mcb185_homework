import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq)) # prints first 30 chars of defline, first 40 char of sequence, and length