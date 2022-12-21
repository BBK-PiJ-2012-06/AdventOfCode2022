input = open('day1/input.txt', 'r')
elfStrings = input.read().split('\n\n')

elves = []
for elfString in elfStrings:
    elfCalories = [int(x) for x in elfString.split('\n')]
    elfTotal = sum(elfCalories)
    elves.append(elfTotal)
print('Part 1:', max(elves))

topThreeSum = 0
for i in range(3): #do sth 3 times
    currentMax = max(elves)
    topThreeSum += currentMax
    elves.remove(currentMax)
print('Part 2:', topThreeSum)
input.close()