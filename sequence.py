# replace T with U
def transcribe(dna):
    return dna.replace('T', 'U')

# finds the reverse-complement strand
def revcomp(dna):
    rc = []
    for nt in dna[::-1]:
        if nt == 'A': rc.append('T')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        elif nt == 'T': rc.append('A')
        else: rc.append('N')
    return ''.join(rc)

# retrieve 3-char codons, convert to aas
def translate(dna):
    aas = []
    for i in range(0, len(dna), 3): # goes thru by threes
        codon = dna[i:i+3] # creates codon
        if codon == 'ATG': aas.append('M')
        elif codon == 'TAA': aas.append('*')
        elif codon == 'TAG': aas.append('*')
        elif codon == 'TGA': aas.append('*')
        else: aas.append('X')
    return ''.join(aas)

# % G and C in sequence
def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)

# difference between # of G and C compared to G + C
def gc_skew(seq):
    c = seq.count('C')
    g = seq.count('G')
    if c + g == 0: return 0
    return (g - c) / (g + c)