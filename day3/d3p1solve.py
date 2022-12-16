rucksacks = open('day3/input.txt', 'r').read().split('\n')

# each rucksack divides evenly into two halves
# find the letter that appears in both halves
# that letter has a priority value a->z = 1->26; A->Z = 27->52
# find the sum of priorities

def getPriorityValue(char):
    if ord('A') <= ord(char) <= ord('Z'):
        return ord(char) - ord('A') + 27

    elif ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a') + 1

prioritySum = 0
for rucksack in rucksacks:
    compartment1 = rucksack[:int(len(rucksack)/2)]
    compartment2 = rucksack[int(len(rucksack)/2):]

    intersection = set(compartment1).intersection(compartment2)
    prioritySum += getPriorityValue(intersection.pop())

print(prioritySum)
