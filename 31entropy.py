1   import sys
2   import math
3
4   probs = []
5   for arg in sys.argv[1:]:
6       f = float(arg)
7       if f <= 0 or f >= 1: sys.exit('error: not a probability')
8       probs.append(float(arg))
9
10  total = 0
11  for p in probs: total += p
12  if not math.isclose(total, 1.0):
13      sys.exit('error: probs must sum to 1.0')
14
15  h = 0
16  for p in probs:
17      h -= p * math.log2(p)
18
19  print(f'{h:.4f}')