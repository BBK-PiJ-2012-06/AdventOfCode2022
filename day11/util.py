import re
from collections import deque

class Monkey:
    def __init__(self, inputStr: str) -> None:
        template = '''Monkey (?P<id>\d+):
  Starting items: (?P<items>.*)
  Operation: new = old (?P<operator>[+*]) (?P<operand>(.*))
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<ifTrue>\d+)
    If false: throw to monkey (?P<ifFalse>\d+)'''
        m = re.match(template, inputStr)
        self.inspectedCount = 0
        self.id = int(m.group('id'))
        startingItems = m.group('items').split(', ')
        self.items = deque(int(x) for x in startingItems)
        self.operator = m.group('operator')
        self.operand = None if m.group('operand') == 'old' else int(m.group('operand'))
        self.test = int(m.group('test'))
        self.ifTrue = int(m.group('ifTrue'))
        self.ifFalse = int(m.group('ifFalse'))