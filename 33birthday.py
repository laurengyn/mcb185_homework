import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0
for i in range(trials):
    birthdays = []
    for i in range(people):
        bday = random.randint(0, days-1)
        if bday in birthdays: 
            shared += 1
            break
        birthdays.append(bday)

print (shared/trials)
