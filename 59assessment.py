import sys
import mcb185

'''
TASK: write a program that when given a fasta file, make a table of aa frequencies 
in a file (such as ecoli proteome)

4 aa wide by 5 aa long that looks like below:

Ala     0.5     |Gln     0       |X       0       |X       0
Arg     0.25    |X       0       |X       0       |X       0
Asn     0.25    |X       0       |X       0       |X       0
Cys     0       |X       0       |X       0       |X       0
Glu     0       |X       0       |X       0       |X       0
'''


three_letter_code = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp',
                        'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
                        'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys',
                        'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
                        'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}

count = {} # empty dictionary
total = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    # general count of aa
    for aa in seq:
        if aa not in count: 
            count[aa] = 0
        count[aa] += 1
        total += 1

for aa in count:
    count[aa] /= total

print(f"{'AA':<5}{'Frequency'}")
#aa_list = list(count.keys())

x = 1
for aa, p in count.items():
    if aa in three_letter_code:
        code = three_letter_code[aa]
    else: 
        code = 'N/A'
    print(f'{code:<5} {100*p:.2f}', end='       ')
    if x % 4 == 0: 
        print()
    x += 1
