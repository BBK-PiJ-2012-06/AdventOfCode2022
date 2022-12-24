input = open('day10/input.txt', 'r')

# X controls horiz position of a sprite, 3 pixels wide (X is pos of center px)
# CRT is 40 px wide and 6px tall. CRT draws a single px each cycle.
# if sprite is visible when px is drawn, draw #, otherwise .
# part 2: what 8 capital letters appear on the CRT? 

program = input

X = 1
sprite = [X-1, X, X+1]
CRT = [[]]
cycle = 0
addx = None
instruction = 'noop'

def executeInstruction():
    global X, addx, instruction, sprite
    if addx:
        X += addx
        sprite = [X-1, X, X+1]
        addx = None
        return

    instruction = program.readline().strip()
    if instruction == 'noop':
        return
    elif instruction:
        addx = int(instruction.split(' ')[1])
        return

def drawPixel():
    line = CRT[-1]
    pixel = '#' if len(line) in sprite else '.'
    line.append(pixel)

while instruction:
    cycle += 1
    drawPixel()
    executeInstruction()
    if (cycle) % 40 == 0:
        # new line
        CRT.append([])

print('\n'.join(' '.join(x for x in line) for line in CRT))
input.close()