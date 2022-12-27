import time
import sys
import re
import json

grid = []
scenicScores = []

def calculateScenicScores(x,y):
    heigth = grid[x][y]
    # print(f"{x},{y},{heigth}")
    scenicScoreUp = 0
    if x > 0:
        for px in range(x-1,-1,-1):
            # print(f"  U Considering {px},{y} heigth {grid[px][y]}. Hides? {heigth <= grid[px][y]}")
            scenicScoreUp+=1
            if heigth <= grid[px][y]:
                break
            
    scenicScoreDown = 0
    if x < xmax:
        for px in range(x+1,xmax):
            # print(f"  D Considering {px},{y} heigth {grid[px][y]}. Hides? {heigth <= grid[px][y]}")
            scenicScoreDown+=1
            if heigth <= grid[px][y]:
                break

    scenicScoreLeft = 0
    if y > 0:
        for py in range(y-1,-1,-1):
            # print(f"  L Considering {x},{py} heigth {grid[x][py]}. Hides? {heigth <= grid[x][py]}")
            scenicScoreLeft+=1
            if heigth <= grid[x][py]:
                break
            
    scenicScoreRight = 0
    if y < ymax:
        for py in range(y+1,ymax):
            # print(f"  R Considering {x},{py} heigth {grid[x][py]}. Hides? {heigth <= grid[x][py]}")
            scenicScoreRight+=1
            if heigth <= grid[x][py]:
                break
            
    # print(f"U{scenicScoreUp}, D{scenicScoreDown}, L{scenicScoreLeft}, R{scenicScoreRight}")
    return scenicScoreUp * scenicScoreDown* scenicScoreLeft* scenicScoreRight

file1 = open('puzzle_input.csv', 'r')
Lines = file1.readlines()
xmax =0 
ymax =0 
for line in Lines:
    xmax = len(line.strip())
    ymax +=1
    grid.append([int(x) for x in line.strip()])

# print(str(xmax) + " by " + str(ymax))

# for x in range(xmax):
#     print(grid[x])
for x in range(xmax):
    for y in range(ymax):
        scenicScores.append(calculateScenicScores(x,y))
print(max(scenicScores))