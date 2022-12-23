input = open('day9/input.txt', 'r')

# simulate rope physics: input is movements of the head, the tail updates to stay touching the head
# (diagonally adjacent and overlapping count as touching)
# part 1: count the number of unique points visited by the tail

movements = input.read().splitlines()

head = [0,0]
tail = [0,0]
visited = { (0,0) }

for move in movements:
    direction, steps = move.split(' ')
    for i in range(int(steps)):
        # update head
        dx = 1 if direction == 'R' else -1 if direction == 'L' else 0
        dy = 1 if direction == 'U' else -1 if direction == 'D' else 0

        head[0] += dx
        head[1] += dy

        #update tail
        _x = head[0] - tail[0]
        _y = head[1] - tail[1]
        
        if abs(_x) == 2:
            tail[0] += _x // 2
            tail[1] = head[1]
        elif abs(_y) == 2:
            tail[1] += _y // 2
            tail[0] = head[0]
        
        visited.add((tail[0], tail[1]))

print("Part 1:", len(visited))

input.close()