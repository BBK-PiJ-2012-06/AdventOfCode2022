input = open('day8/input.txt', 'r')

# input is a square grid of tree heights. a tree is visible from outside the grid if it is 
# taller than all trees between itself and the edge of the grid, in any of the cardinal directions 
# (all trees on the edge of the grid are visible).
# part 1: count the number of visible trees.

# thoughts: parse into 2d array. for each element:
# if either index = 0 or max -> count it (2*width + 2*height - 4)
# otherwise, start checking. optimise by checking shortest distance first (horiz then vert?)

grid = [list(map(int, line)) for line in input.read().splitlines()]

def isVisible(x, y):
    return (visibleFromNorth(x, y) 
        or visibleFromEast(x, y) 
        or visibleFromSouth(x, y) 
        or visibleFromWest(x, y))

def visibleFromNorth(x, y):
    for row in grid[:y]:
        if row[x] >= grid[y][x]:
            return False
    return True

def visibleFromEast(x, y):
    for tree in grid[y][x+1:]:
        if tree >= grid[y][x]:
            return False
    return True

def visibleFromSouth(x, y):
    for row in grid[y+1:]:
        if row[x] >= grid[y][x]:
            return False
    return True

def visibleFromWest(x, y):
    for tree in grid[y][:x]:
        if tree >= grid[y][x]:
            return False
    return True

lenY = len(grid)
lenX = len(grid[0])
nVisible = 2*lenY + 2*lenX - 4

for y in range(lenY)[1:-1]:
    for x in range(lenX)[1:-1]:        
        nVisible += isVisible(x, y)

print("Part 1:", nVisible)
input.close()