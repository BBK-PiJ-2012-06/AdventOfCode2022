input = open('day10/input.txt', 'r')

# signal strength = cycle * X
# part 1: calc the sum of sig strengths for the 20th, 60th, 100th, 140th, 180th
# and 220th cycles. 

program = input

X = 1
cycle = 0
addx = None
instruction = 'noop'
part1sum = 0

while instruction:
    cycle += 1
    if (cycle-20) % 40 == 0:
        print('cycle:', cycle, '\tX:', X) 
        part1sum += cycle * X

    if addx:
        X += addx
        addx = None
        continue

    instruction = program.readline().strip()
    if instruction == 'noop':
        continue
    elif instruction:
        addx = int(instruction.split(' ')[1])
        continue

print("Part 1:", part1sum)

input.close()