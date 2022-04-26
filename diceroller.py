# Roll a dice with M sides N times
import random
sides = int(input("Enter the number of sides: "))
rolls = int(input("Enter the number of rolls: "))
counts = []
for i in range(sides):
    counts.append(0)

for i in range(rolls):
    roll = random.randint(1, sides)
    counts[roll - 1] += 1

for i in range(sides):
    print(f"{i + 1}: {counts[i]}")