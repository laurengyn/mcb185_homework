import sys
import sequence

seq = 'AAAAAAAAAAGGGGGGGGGGTTTTTTTTTTCCCCCCCCCC'
w = 10 # window

# initial window, counts amount of G and C in window
s = seq[:w]
g_count = s.count('G')
c_count = s.count('C')
print(0, sequence.gc_comp(s), sequence.gc_skew(s)) # prints index, comp, and skew

# sliding window
for i in range (1, len(seq) - w + 1): # similar to 43skew minus the first window
    # nt moving out of window
    if seq[i-1] == 'G': g_count -= 1 # if the nt going out of window is G
    elif seq[i-1] == 'C': c_count -= 1 # if the nt going out of the window is C
    # nt moving into window
    if seq[i + w - 1] == 'G': g_count += 1 # if the nt going into the window is G
    elif seq[i + w - 1] == 'C': c_count += 1 # if the nt going into the window is C
    s = seq[i:i + w] # changes to new window
    print(i, sequence.gc_comp(s), sequence.gc_skew(s))