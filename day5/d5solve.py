# first part of input represents the arrangement of crates
# second part of input is instructions to move them around
# part 1: find out which crate is at the top of each stack after the instructions have been carried out

# parse crates into stack-like structures => movements nicely map to popping and pushing on stacks
# deque is apparently a stack impl that performs better than a list
from collections import deque
import re #regex

def getStacks(stackStr):
    stackStr = stackStr.split('\n')
    nStacks = int(stackStr.pop().rstrip()[-1])
    
    stacks = [deque() for i in range(nStacks)]

    while stackStr:
        layer = stackStr.pop()
        crates = [layer[i:i+4] for i in range(0, len(layer), 4)] # each crate takes 4 chars, e.g. '[X] '
        
        for i in range(nStacks):
            crate = crates[i]
            contents = crate[1]
            if not(contents.isspace()):
                stacks[i].append(contents)
    return(stacks)

def peekStacks(stacks):
    peek = ''
    for stack in stacks:
        peek += stack[-1]
    return peek

stackStr, instructionsStr = open('day5/input.txt', 'r').read().split('\n\n')
stacks = getStacks(stackStr)

instructions = instructionsStr.split('\n')
for instruction in instructions:
    numberToMove, src, dest = re.findall('\d+', instruction)
    
    srcIndex = int(src)-1
    destIndex = int(dest)-1

    for i in range(int(numberToMove)):
        stacks[destIndex].append(stacks[srcIndex].pop())
    
print('Part1:', peekStacks(stacks))
