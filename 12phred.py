"""
Write functions that convert quality value symbols into error rates and vice-versa. 
The ord() function returns the ASCII value of a letter. 
The chr() function turns an ASCII value into a letter.

Demonstrate the functions work by calling them several times. Edge cases should return None.
"""

import math

def char_to_prob(char):
    if len(char) == 1 and 33 <= ord(char) <= 126:
        return (10 ** (-(ord(char) - 33)/10))
    return None


def prob_to_char(num):
    if 0 < num <= 1: 
        ascii_value = round ((-10 * math.log10(num)) + 33)
        if 33 <= ascii_value <= 126:
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