input = open('day5/input.txt', 'r')

# first part of input represents the arrangement of crates
# second part of input is instructions to move them around 
# part 1: find out which crate is at the top of each stack after the instructions have been carried out
# the crane, "CrateMover9000" can only move 1 crate at a time

import re #regex
from util import * 

stackStr, instructionsStr = input.read().split('\n\n')
stacks = getStacks(stackStr)

instructions = instructionsStr.split('\n')
crane = CrateMover9000()

for instruction in instructions:
    numberToMove, src, dest = re.findall('\d+', instruction) # e.g. 'move 11 from 8 to 2'
    
    srcIndex = int(src)-1
    destIndex = int(dest)-1

    crane.moveCrates(stacks[srcIndex], stacks[destIndex], int(numberToMove))
    
print('Part1:', peekStacks(stacks))

input.close()