import time
import sys
import re
import json

grid = []

def isVisible(x,y):
    value = grid[x][y]
    # print(f"{x},{y},{value}")
    if x == 0 or x == xmax-1 or y==0 or y == ymax-1:
        # print("  on perifery")
        return True
    returnVal = True
    hiddenUp = False
    hiddenDown = False
    hiddenLeft = False
    hiddenRight = False
    for px in range(x):
        # print(f"  Considering {px},{y} value {grid[px][y]}. Hides? {value <= grid[px][y]}")
        hiddenUp = hiddenUp or value <= grid[px][y]
    for px in range(x+1,xmax):
        # print(f"  Considering {px},{y} value {grid[px][y]}. Hides? {value <= grid[px][y]}")
        hiddenDown = hiddenDown or value <= grid[px][y]
    for py in range(y):
        # print(f"  Considering {x},{py} value {grid[x][py]}. Hides? {value <= grid[x][py]}")
        hiddenLeft = hiddenLeft or value <= grid[x][py]
    for py in range(y+1,ymax):
        # print(f"  Considering {x},{py} value {grid[x][py]}. Hides? {value <= grid[x][py]}")
        hiddenRight = hiddenRight or value <= grid[x][py]
    # print(f"U{hiddenUp} D{hiddenDown} L{hiddenLeft} R{hiddenRight}")
    return not (hiddenUp and hiddenDown and hiddenLeft and hiddenRight)

file1 = open('puzzle_input.csv', 'r')
Lines = file1.readlines()
xmax =0 
ymax =0 
for line in Lines:
    xmax = len(line.strip())
    ymax +=1
    grid.append([int(x) for x in line.strip()])

# print(str(xmax) + " by " + str(ymax))

result = 0
# for x in range(xmax):
    # print(grid[x])
for x in range(xmax):
    for y in range(ymax):
        if isVisible(x,y):
            result += 1
print(result)