from util import dijkstraReversed
input = open('day12/input.txt', 'r')

# we can do this faster by starting from 'E' and stopping at the first 'a' we reach

heightMap = [list(x for x in line) for line in input.read().splitlines()]
start = ()
for i, row in enumerate(heightMap):
    for j, height in enumerate(row):
        if height == 'E': start = (i, j)

distance = dijkstraReversed(heightMap, 'a', start)

print("Part 2:", distance)

input.close()