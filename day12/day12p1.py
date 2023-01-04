input = open('day12/input.txt', 'r')

# input is heightmap, elevation rep'd by letter a(lowest)-z(heighest)
# start = S = a, end = E = z
# go from S to E in fewest steps: part 1 ans = how many steps? 
# can move up, down, left, right, 1 square at a time
# if square elevation is > 1 higher than current, cannot move there

# let's try to implement Dijkstra's algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

grid = [list(x for x in line) for line in input.read().splitlines()]

unvisited = {} 
visited = {}
destination = ()
current = ()
currentDistance = 0
for i, row in enumerate(grid):
    unvisited[i] = {}
    visited[i] = {} 
    for j, col in enumerate(row):
        if col == 'S':
            current = (i, j)
            unvisited[i][j] = currentDistance
        else:
            unvisited[i][j] = 'inf' # infinite distance
        if col == 'E':
            destination = (i, j)

print(f'dest: {destination}')
while True:
    # for current, consider all unvisited neighbours
    ci, cj = current
    for (i,j) in [(ci-1,cj), (ci+1,cj), (ci,cj-1), (ci,cj+1)]:
        neighbour = unvisited.get(i, {}).get(j)
        if neighbour is None: continue
        
        # calculate tentative distance through the current node if accessible
        neighbourHeight = ord('z') if grid[i][j] == 'E' else ord(grid[i][j])
        currentHeight = ord('a') if grid[ci][cj] == 'S' else ord(grid[ci][cj])
        if neighbourHeight <= currentHeight + 1:
            if unvisited[i][j] == 'inf' or (currentDistance + 1 < unvisited[i][j]):
                unvisited[i][j] = currentDistance + 1
    
    # mark the current node as visited and remove it from the unvisited set
    visited[ci][cj] = currentDistance
    del unvisited[ci][cj]
    
    # If the destination node has been marked visited, stop      
    if visited.get(destination[0], {}).get(destination[1]): break
   
    # Otherwise, select the unvisited node that is marked with the smallest tentative distance
    candidates = []
    for i, row in unvisited.items():
        if isinstance(row, dict):
            for j, col in row.items():
                if col != 'inf':
                    candidates.append((i, j, unvisited[i][j]))
    topCandidate = sorted(candidates, key = lambda x: x[2])[0]
    current = (topCandidate[0], topCandidate[1])
    currentDistance = topCandidate[2]

print("Part 1:", visited[destination[0]][destination[1]])

input.close()