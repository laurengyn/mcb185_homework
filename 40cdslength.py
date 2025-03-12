'''
IN TERMINAL: specify path to file

TASK: 
1. Skip over comment lines
2. Find CDS features (or skip over all non-CDS features)
3. Extract the begin and end coordinates
4. Convert the coordinates to integers
5. Report the length of the CDS (end - begin + 1)
'''
import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue # skips over comment lines, continue skips line to next iteration
        words = line.split()
        if words[2] != 'CDS': continue # find CDS features
        beg = int(words[3]) # extract beginning coordinate + converts to integer
        end = int(words[4]) # extract ending coordinate + converts to integer
        print(end - beg + 1) # report length of CDS