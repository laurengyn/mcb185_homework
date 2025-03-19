import sys
import argparse
import mcb185
import math
'''
parser = argparse.ArgumentParser(description='DNA entropy filter.') # creates argument parser object in variable 'parser'
parser.add_argument('file', type=str, help='name of fasta file') # positional argument for path to fasta file
parser.add_argument('size', type=int, help='window size') # positional argument for window  size that is integer
parser.add_argument('entropy', type=float, help='entropy threshold') # positional argumeent for entropy threshold that is float
arg = parser.parse_args() # creats arg object by harvesting values on command line and assigning to various properties
print('dusting with', arg.file, arg.size, arg.entropy)
'''

'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20, # CHANGE: --size means it is optional
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4, # CHANGE: --entropy means it is optional
    help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''

'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask') # CHANGE: acts like a flag to enable/disable features
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)
'''

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, # CHANGE: --size = -s
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, # CHANGE: --entropy = -e
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

def entropy(seq):
    counts = {} # empty dictionary
    for nt in seq:
        if nt in counts: counts[nt] += 1 # if nt was already sseen
        else: counts[nt] = 1 # if nt is new
    total = len(seq) # total nt in window
    h = 0 # entropy
    for nt in counts:
        p = counts[nt]/total # probability of each nt
        h -= p + math.log2(p) # entropy formula
    return h

for defline, seq in mcb185.read_fasta(arg.file):
    masked_seq = list(seq) 
    for i in range(len(seq) - arg.size + 1): # sliding window
        window = seq[i:i + arg.size]
        h = entropy(window) # entropy of window
        if h < arg.entropy:
            if arg.lower: masked_seq[i:i + arg.size] = window.lower() # above threshold
            else: masked_seq[i:i + arg.size] = 'N' * arg.size # below threshold
    
    print(f'>{defline}')
    for i in range(0, len(masked_seq), 60):
        print(''.join(masked_seq[i:i+60]))