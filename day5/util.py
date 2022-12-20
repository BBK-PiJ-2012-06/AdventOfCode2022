# parse crates into stack-like structures => movements nicely map to popping and pushing on stacks
# deque is apparently a stack impl that performs better than a list

from collections import deque

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

class CrateMover9000: # can only move one crate at a time
    def moveCrates(self, src, dest, numberToMove):
        for i in range(numberToMove):
            dest.append(src.pop())

class CrateMover9001: # can move multiple crates at once
    def __init__(self):
        self.crane = deque() # the crane grabber acts as an intermediary stack

    def moveCrates(self, src, dest, numberToMove):
        for i in range(numberToMove):
            self.crane.append(src.pop())
        for i in range(numberToMove):
            dest.append(self.crane.pop())