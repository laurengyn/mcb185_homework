import math

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper()) ## all uppercase
print(s)

print(s.replace('o', '')) ## removes all o's
print(s.replace('o', '').replace('r', 'i')) ## removes all o's, replaces r's with i's

print('STRING FORMATTING')

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":>30}')
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify
print(f'{20:<20} {10}') 

print('{} {:.3f}'.format('str.format', math.pi))
print('{} {:.5f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))
print('%s %.5f' % ('printf', math.pi))