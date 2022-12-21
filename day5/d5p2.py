input = open('day5/input.txt', 'r')

# first part of input represents the arrangement of crates
# second part of input is instructions to move them around 
# part 2: find out which crate is at the top of each stack after the instructions have been carried out
# the crane, "CrateMover9001" can now move multiple crates at once

import re 
from util import * 

stackStr, instructionsStr = input.read().split('\n\n')
stacks = getStacks(stackStr)

instructions = instructionsStr.split('\n')
crane = CrateMover9001()

for instruction in instructions:
    numberToMove, src, dest = re.findall('\d+', instruction) # e.g. 'move 11 from 8 to 2'
    
    srcIndex = int(src)-1
    destIndex = int(dest)-1

    crane.moveCrates(stacks[srcIndex], stacks[destIndex], int(numberToMove))

print('Part2:', peekStacks(stacks))

input.close()