"""
Write a function that returns the oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo. Use these two methods.

For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
Demonstrate that your program works by computing the Tm of several oligos of different sizes.
"""

def tm(a, c, g, t):
    if (a+c+g+t) <= 13: return ((a+t)*2 + (g+c)*4)
    else: return 64.9 + 41*(g+c -16.4) / (a+t+g+c)

print (tm(1, 1, 1, 1))
print (tm(3, 3, 3, 3))
print (tm(3, 3, 3, 4))
print (tm(3, 3, 4, 4))
print (tm(4, 4, 4, 4))