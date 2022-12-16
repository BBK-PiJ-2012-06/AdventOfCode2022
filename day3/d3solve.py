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

part1 = 0
for rucksack in rucksacks:
    compartment1 = rucksack[:int(len(rucksack)/2)]
    compartment2 = rucksack[int(len(rucksack)/2):]

    part1 += getPriorityValue(set(compartment1).intersection(compartment2).pop())

print("Part 1:", part1)

# each sequential group of 3 rucksacks has a single item in common
# sum the priority values for each of these items

part2 = 0
while rucksacks:
    elf1 = rucksacks.pop()
    elf2 = rucksacks.pop()
    elf3 = rucksacks.pop()
    
    part2 += getPriorityValue(set(elf1).intersection(elf2).intersection(elf3).pop())

print("Part 2:", part2)
