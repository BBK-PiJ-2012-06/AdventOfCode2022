input = open('day11/input.txt', 'r')

from util import Monkey

monkeyStrs = input.read().split('\n\n')
monkeys = []

for monkeyStr in monkeyStrs:
    monkeys.append(Monkey(monkeyStr))

for round in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.popleft()
            monkey.inspectedCount += 1
            #operate, divide by 3 and round down, test, throw
            if monkey.operator == '*':
                item *= item if monkey.operand is None else monkey.operand
            if monkey.operator == '+':
                item += item if monkey.operand is None else monkey.operand
            item = item // 3
            if item % monkey.test == 0:
                monkeys[monkey.ifTrue].items.append(item)
            else:
                monkeys[monkey.ifFalse].items.append(item)

sortedCounts = sorted([x.inspectedCount for x in monkeys])
monkeyBusiness = sortedCounts[-1] * sortedCounts[-2]
print("Part 1:", monkeyBusiness)

input.close()