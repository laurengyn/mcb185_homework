# python3 ~/Code/mcb185_homework/48transmembrane.py ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz
import sys
import mcb185

# Kyte-Doolittle hydrophobicity
def calc(window):
    hydrophobicity = 0
    # aas and their kd hp value
    amino = 'ACDEFGHIKLMNPQRSTVWY'
    aminohs = [1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3]

    for aa in range(len(window)):
        hydrophobicity += aminohs[amino.find(window[aa])] # calculates hp sum in window
    return hydrophobicity/len(window) # avg hp value in window

# check for hydrophobic region in sequence
def hp(seq, w, t): # sequence, window size, threshold
    signal = False
    for i in range(len(seq) - w + 1): 
        window = seq[i: i+w] # sets window sizw
        if 'P' in window: continue # skips proline
        elif calc(window) < t: continue # skips if avg kd is lower than threshold
        else: return True # valid region found
    return False # no valid region found

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    words = defline.split()
    name = words[0] # protein id
    if hp(seq[0:30], 8, 2.5) and hp(seq[30:], 11, 2.0): # checks for transmembrane region after 30 aa
        print (defline)