from util import dijkstra
input = open('day12/input.txt', 'r')

# part 2: find the shortest distance to E from *any* starting point of height 'a'

heightMap = [list(x for x in line) for line in input.read().splitlines()]
startNodes = []
destination = ()
for i, row in enumerate(heightMap):
    for j, height in enumerate(row):
        if height == 'S': startNodes.append((i, j))
        if height == 'a': startNodes.append((i, j))
        if height == 'E': destination = (i, j)

distances = []
for startNode in startNodes:
    distance = dijkstra(heightMap, destination, startNode)
    if distance: distances.append(distance)

print("Part 2:", min(distances))

input.close()