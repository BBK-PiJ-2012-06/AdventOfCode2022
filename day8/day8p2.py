input = open('day8/input.txt', 'r')

# a tree's viewing distance in a particular direction is the number of trees in that direction until 
# reaching a tree of equal or greater height e.g. going right from 3 in 322145, vDist = 4.
# a tree's *scenic score* is found by multiplying its 4 viewing distances together. 
# part 2: find the greatest scenic score for all trees in the input.

grid = [list(map(int, line)) for line in input.read().splitlines()]

def getScenicScore(x, y):
    return (viewingDistanceNorth(x, y) 
        * viewingDistanceEast(x, y) 
        * viewingDistanceSouth(x, y) 
        * viewingDistanceWest(x, y))

def viewingDistanceNorth(x, y):
    viewDist = 0
    for row in reversed(grid[:y]):
        viewDist += 1
        if row[x] >= grid[y][x]:
            break
    return viewDist

def viewingDistanceEast(x, y):
    viewDist = 0
    for tree in grid[y][x+1:]:
        viewDist += 1
        if tree >= grid[y][x]:
            break
    return viewDist

def viewingDistanceSouth(x, y):
    viewDist = 0
    for row in grid[y+1:]:
        viewDist += 1
        if row[x] >= grid[y][x]:
            break
    return viewDist

def viewingDistanceWest(x, y):
    viewDist = 0
    for tree in reversed(grid[y][:x]):
        viewDist += 1
        if tree >= grid[y][x]:
            break
    return viewDist

lenY = len(grid)
lenX = len(grid[0])
maxScenicScore = 0

for y in range(lenY):
    for x in range(lenX):
        scenicScore = getScenicScore(x, y)
        maxScenicScore = max(maxScenicScore, scenicScore)       

print("Part 2:", maxScenicScore)
input.close()