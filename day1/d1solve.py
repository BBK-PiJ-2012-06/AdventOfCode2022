elfStrings = open('day1/input.txt', 'r').read().split('\n\n')

elves = []
print('Part 1:')
for elfString in elfStrings:
    elfCalories = [int(x) for x in elfString.split('\n')]
    elfTotal = sum(elfCalories)
    elves.append(elfTotal)
print(max(elves))
print('\n')

print('Part 2:')
topThreeSum = 0
for i in range(3): #do sth 3 times
    currentMax = max(elves)
    topThreeSum += currentMax
    elves.remove(currentMax)
print(topThreeSum)