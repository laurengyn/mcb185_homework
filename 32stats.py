import math
import sys

# grabbing values, converting to numbers
stats = []
for arg in sys.argv[1:]:
    f = float(arg)
    stats.append(float(arg))

# finding min, max, sum
min_val = stats[0]
max_val = stats[0]
total_sum = stats[0]
for i in stats[1:]:
    total_sum += i
    if i < min_val: min_val = i
    if i > max_val: max_val = i

# finding mean, standev
mean = total_sum/len(stats)
stan_dev_sum = 0
for i in stats:
    stan_dev_sum += ((i - mean) ** 2)
stan_dev = math.sqrt(stan_dev_sum/len(stats))

# finding median
stats.sort()
if len(stats) % 2 == 1: median = stats[len(stats)//2]
else: median = (stats[len(stats)//2 -1] + stats[len(stats)//2]) / 2

print ('the number of values is', len(stats))
print ('the minimum value is', min_val)
print ('the maximum value is', max_val)
print ('the mean is', mean)
print ('the standard deviation is', stan_dev)
print ('the median is', median)