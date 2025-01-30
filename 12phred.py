"""
Write functions that convert quality value symbols into error rates and vice-versa. 
The ord() function returns the ASCII value of a letter. 
The chr() function turns an ASCII value into a letter.

Demonstrate the functions work by calling them several times. Edge cases should return None.
"""

import math

def char_to_prob(a):
    if ord(a) >= 32 and ord(a) <= 126:
        return (10 ** (-(ord(a) - 33)/10))
    return None


def prob_to_char(num):
    if num <= 1 and num > 0: 
        ascii_value = round ((-10 * math.log10(num)) + 33)
        if  ascii_value >= 32 and ascii_value <= 126:
            return chr (ascii_value) 
    return None

print("Testing char_to_prob")
print(char_to_prob('A'))
print(char_to_prob('!'))
print(char_to_prob('~'))
print(char_to_prob(' '))   
print(char_to_prob('AA'))

print("Testing prob_to_char")
print(prob_to_char(0.001))
print(prob_to_char(0.1))
print(prob_to_char(1.0))
print(prob_to_char(1.1))
print(prob_to_char(-0.1))