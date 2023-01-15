import time
import sys
import re
import json

Monkeys = []

def multiply(old, by):
    return old*by
def multiplySelf(old, by):
    return old*old
def add(old, by):
    return old+by

class Monkey():
    def __init__(self, items, operation, secondParam, testDivBy, trueThrowTo, falseThrowTo):
        self.items = items
        self.operation = operation
        self.secondParam = secondParam
        self.testDivBy = testDivBy
        self.trueThrowTo = trueThrowTo
        self.falseThrowTo = falseThrowTo
    inspectCount = 0 
    items = []
    operation = ""
    secondParam = 0
    testDivBy = 1
    trueThrowTo= 1
    falseThrowTo= 1
    def perform_operation(self, item):
        wl = item
        item = int(self.operation(wl, self.secondParam) / 3)
        global Monkeys
        if item%self.testDivBy == 0:
            Monkeys[self.trueThrowTo].items.append(item)
        else:
            Monkeys[self.falseThrowTo].items.append(item)
    def throwAllItems(self):
        i = self.items
        for item in i:
            self.inspectCount+=1
            self.perform_operation(item)
        self.items.clear()


m0 =  Monkey([74, 73, 57, 77, 74], multiply, 11, 19,6,7)
m1 =  Monkey([99, 77, 79], add, 8, 2,6,0)
m2 =  Monkey([64, 67, 50, 96, 89, 82, 82], add, 1, 3,5,3)
m3 =  Monkey([88], multiply, 7, 17,5,4)
m4 = Monkey([80, 66, 98, 83, 70, 63, 57, 66], add, 4, 13, 0,1)
m5 = Monkey([81, 93, 90, 61, 62, 64], add, 7,7,1,4)
m6 = Monkey([69, 97, 88, 93],multiplySelf, 0, 5,7,2)
m7 = Monkey([59, 80], add, 6, 11,2,3)

Monkeys.append(m0)
Monkeys.append(m1)
Monkeys.append(m2)
Monkeys.append(m3)
Monkeys.append(m4)
Monkeys.append(m5)
Monkeys.append(m6)
Monkeys.append(m7)
for i in range(20):
    for m in Monkeys:
        m.throwAllItems()

Monkeys.sort(key=lambda x: x.inspectCount, reverse=True)

sum = 1
for monkey in Monkeys[0:2]:
    sum *= monkey.inspectCount
print(sum)