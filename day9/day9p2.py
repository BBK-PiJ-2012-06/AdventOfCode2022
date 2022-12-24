input = open('day9/input.txt', 'r')

# part 2: now the rope consists of 10 knots, all moving as per the previous rules;
# again, count the number of unique points visited by the tail
# new moves are possible now! i.e. when a diagonally-adjacent section moves diagonally:
# . . x                  . . H
# . H .  H moves to x -> . T .
# T . .                  . . .

movements = input.read().splitlines()

rope = [[0,0] for _ in range(10)]
head = rope[0]
tail = rope[-1]

def drawRope(): # just for debugging / fun :D
    maxX = max(r[0] for r in rope)
    minX = min(r[0] for r in rope)
    maxY = max(r[1] for r in rope)
    minY = min(r[1] for r in rope)
    w = maxX - minX
    h = maxY - minY
    grid = [['.' for i in range(w+1)] for j in range(h+1)]
    for idx, r in enumerate(rope):
        x = r[0] - minX
        y = r[1] - minY
        grid[y][x] = idx
    print('-------')
    print('\n'.join(' '.join(str(x) for x in line) for line in reversed(grid)))
    
visited = { (0,0) }
for move in movements:
    direction, steps = move.split(' ')
    for _ in range(int(steps)):
        # update head
        dx = 1 if direction == 'R' else -1 if direction == 'L' else 0
        dy = 1 if direction == 'U' else -1 if direction == 'D' else 0

        head[0] += dx
        head[1] += dy

        #update rest of rope
        for i in range(1, len(rope)):
            t = rope[i]
            h = rope[i-1]
            _x = h[0] - t[0]
            _y = h[1] - t[1]
        
            if abs(_x) == 2 and abs(_y) == 2:
                t[0] += _x // 2
                t[1] += _y // 2
            elif abs(_x) == 2:
                t[0] += _x // 2
                t[1] = h[1]
            elif abs(_y) == 2:
                t[1] += _y // 2
                t[0] = h[0]
        
        visited.add(tuple(tail))
        #drawRope()

print("Part 2:", len(visited))
drawRope()
input.close()