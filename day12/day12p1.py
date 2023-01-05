input = open('day12/input.txt', 'r')

# input is heightmap, elevation rep'd by letter a(lowest)-z(heighest)
# start = S = a, end = E = z
# go from S to E in fewest steps: part 1 ans = how many steps? 
# can move up, down, left, right, 1 square at a time
# if square elevation is > 1 higher than current, cannot move there

# let's try to implement Dijkstra's algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

from util import dijkstra

heightMap = [list(x for x in line) for line in input.read().splitlines()]

destination = ()
start = ()
for i, row in enumerate(heightMap):
    for j, height in enumerate(row):
        if height == 'S': start = (i, j)
        if height == 'E': destination = (i, j)

shortestDistance = dijkstra(heightMap, destination, start)

print("Part 1:", shortestDistance)

input.close()