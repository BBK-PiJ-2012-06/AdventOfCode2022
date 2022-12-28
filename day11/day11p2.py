input = open('day11/input.txt', 'r')

from util import Monkey
from functools import reduce

monkeyStrs = input.read().split('\n\n')
monkeys = []

for monkeyStr in monkeyStrs:
    monkeys.append(Monkey(monkeyStr))

# use the Chinese remainder theorem
testProduct = reduce(lambda x, y: x*y, [m.test for m in monkeys])

for round in range(10_000):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.popleft()
            monkey.inspectedCount += 1
            #operate, find remainder mod testProduct, test, throw
            if monkey.operator == '*':
                item *= item if monkey.operand is None else monkey.operand
            if monkey.operator == '+':
                item += item if monkey.operand is None else monkey.operand
            item = item % testProduct
            if item % monkey.test == 0:
                monkeys[monkey.ifTrue].items.append(item)
            else:
                monkeys[monkey.ifFalse].items.append(item)

sortedCounts = sorted([x.inspectedCount for x in monkeys])
monkeyBusiness = sortedCounts[-1] * sortedCounts[-2]
print("Part 2:", monkeyBusiness)

input.close()