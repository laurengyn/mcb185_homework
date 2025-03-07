'''
Write a program that provides the closest official color name given some red, green, and blue values. 
For example, given the color values 200, 0, 50, your program should report a shade of red. 
You will find color definitions in the colors_basic.tsv and colors_extended.tsv in MCB185/data.
'''

import sys
import gzip

colorfile = sys.argv[1]
R = int(sys.argv[2]) # red val
G = int(sys.argv[3]) # green val
B = int(sys.argv[4]) # blue val

# taxi cab diff
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

smallest_dist = int(10000000)
closest_color = None
with open(colorfile) as fp:
    for line in fp:
        parts = line.split('\t') # splits up the table
        if len(parts) != 3: continue # if there aren't 3 parts, skip
        color_name = parts[0]
        color_rgb = parts[2].split(',') # splits up the rgb vals

        color_r = int(color_rgb[0])
        color_g = int(color_rgb[1])
        color_b = int(color_rgb[2])

        # use taxi cab to find the closest color
        distance = dtc((R, G, B), (color_r, color_g, color_b))
        if distance < smallest_dist:
            smallest_dist = distance
            closest_color = color_name
    
    print(smallest_dist, closest_color)