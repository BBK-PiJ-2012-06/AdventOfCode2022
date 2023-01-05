def dijkstra(heightMap, destination, start) -> int:
    unvisited = {}
    visited = {}
    currentDistance = 0
    current = start
    for i, row in enumerate(heightMap):
        unvisited[i] = {}
        visited[i] = {} 
        for j, _ in enumerate(row):
            unvisited[i][j] = 'inf' # infinite distance
    
    unvisited[start[0]][start[1]] = currentDistance

    while True:
        # for current, consider all unvisited neighbours
        ci, cj = current
        for (i,j) in [(ci-1,cj), (ci+1,cj), (ci,cj-1), (ci,cj+1)]:
            if unvisited.get(i, {}).get(j) is None: continue # edge detection
        
            # calculate tentative distance through the current node 
            neighbourHeight = ord('z') if heightMap[i][j] == 'E' else ord(heightMap[i][j])
            currentHeight = ord('a') if heightMap[ci][cj] == 'S' else ord(heightMap[ci][cj])
            if neighbourHeight <= currentHeight + 1: # if node is accessible
                if unvisited[i][j] == 'inf' or (currentDistance + 1 < unvisited[i][j]): # save smallest tentative distance
                    unvisited[i][j] = currentDistance + 1
    
        # mark the current node as visited and remove it from the unvisited set
        visited[ci][cj] = currentDistance
        del unvisited[ci][cj]
    
        # if the destination node has been marked visited, stop
        di, dj = destination      
        if visited.get(di, {}).get(dj): return visited[di][dj]
   
        # otherwise, select the unvisited node that is marked with the smallest tentative distance
        candidates = []
        for i, row in unvisited.items():
            if isinstance(row, dict):
                for j, height in row.items():
                    if height != 'inf':
                        candidates.append((i, j, unvisited[i][j])) # (coordinates, distance)
        
        if not candidates: return None # no route possible
        topCandidate = sorted(candidates, key = lambda x: x[2])[0] # sort by distance
        current = (topCandidate[0], topCandidate[1])
        currentDistance = topCandidate[2]

def dijkstraReversed(heightMap, destinationHeight, start) -> int:
    unvisited = {}
    visited = {}
    currentDistance = 0
    current = start
    for i, row in enumerate(heightMap):
        unvisited[i] = {}
        visited[i] = {} 
        for j, _ in enumerate(row):
            unvisited[i][j] = 'inf' # infinite distance
    
    unvisited[start[0]][start[1]] = currentDistance

    while True:
        # for current, consider all unvisited neighbours
        ci, cj = current
        for (i,j) in [(ci-1,cj), (ci+1,cj), (ci,cj-1), (ci,cj+1)]:
            if unvisited.get(i, {}).get(j) is None: continue # edge detection
        
            # calculate tentative distance through the current node 
            neighbourHeight = ord('z') if heightMap[i][j] == 'E' else ord(heightMap[i][j])
            currentHeight = ord('a') if heightMap[ci][cj] == 'S' else ord(heightMap[ci][cj])
            if neighbourHeight >= currentHeight - 1: # if node is accessible
                if unvisited[i][j] == 'inf' or (currentDistance + 1 < unvisited[i][j]): # save smallest tentative distance
                    unvisited[i][j] = currentDistance + 1
    
        # mark the current node as visited and remove it from the unvisited set
        visited[ci][cj] = currentDistance
        del unvisited[ci][cj]
    
        # if the destination height has been reached, stop
        if currentHeight == ord(destinationHeight): return currentDistance
   
        # otherwise, select the unvisited node that is marked with the smallest tentative distance
        candidates = []
        for i, row in unvisited.items():
            if isinstance(row, dict):
                for j, height in row.items():
                    if height != 'inf':
                        candidates.append((i, j, unvisited[i][j])) # (coordinates, distance)
        
        if not candidates: return None # no route possible
        topCandidate = sorted(candidates, key = lambda x: x[2])[0] # sort by distance
        current = (topCandidate[0], topCandidate[1])
        currentDistance = topCandidate[2]