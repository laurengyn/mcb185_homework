import sys
import mcb185

def find_orfs(seq, min_length): # sequence and minimum valid length
    orfs = []
    stop = ['TAA', 'TAG', 'TGA']
    for frame in range(3): # reading frames
        i = frame
        while i < len(seq):
            if seq[i:i+3] == 'ATG': # start codon
                start = i # note the start
                i += 3
                while i + 2 < len(seq): # so it doesn't go over possible end
                    if seq[i:i +3] in stop: # if there is stop codon
                        end = i + 3 # note the end
                        if end - start >= min_length: # if minimum length is met
                            orfs.append((start, end, frame, '+')) 
                        break
                    i += 3 # next codon
            else: i += 3 # if no start, move to next codon
    return orfs

def find_revorfs(seq, min_length):
    rev_seq = mcb185.anti_seq(seq) # convert seq to reverse comp
    rev_orf = find_orfs(rev_seq, min_length)
    return [(start, end, frame, '-') for start, end, frame, _ in rev_orfs]

def generate_gff(orfs, seq_id):
    gff_output = [] # gff lines
    for start, end, frame, strand in orfs: # loop thru orfs
        gff_output.append(f"{seq_id}\tgene\tCDS\t{start+1}\t{end}\t.\t{strand}\t.\tID=gene{start+1}-{end}") # gff line format
    return gff_output

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    forward = find_orfs(seq, 300)
    reverse = find_revorfs(seq, 300)
    all_orfs = forward + reverse
    gff_output = generate_gff(all_orfs, defline)
    for line in gff_output: print (line)