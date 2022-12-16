pairAssignments = open('day4/input.txt', 'r').read().split('\n')

# each pair is assigned a range of values, e.g. 2-3,6-8
# need to count how many assignments have one range fully containing the other, e.g. 3-4,2-4

part1 = 0
for pairAssignment in pairAssignments:
    r1Str, r2Str = pairAssignment.split(',')
    
    range1 = [int(x) for x in r1Str.split('-')]
    range2 = [int(x) for x in r2Str.split('-')]

    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        part1 += 1

    elif range2[0] <= range1[0] and range2[1] >= range1[1]:
        part1 += 1

print("Part 1:", part1)