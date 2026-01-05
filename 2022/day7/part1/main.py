import time
import sys
import re
import json

fs = {}
currentDir = {}
largeDicts= []

def calcSize(d, indent=0):
   returnVal = 0
   for key, value in d.items():
      if key == "..":
         i = 0
      else: 
        if isinstance(value, dict):
             dictSize = calcSize(value, indent+1)
             if dictSize <= 100000:
                largeDicts.append(dictSize)
             returnVal += dictSize
        else:
            returnVal += value
   return returnVal

file1 = open('puzzle_input.csv', 'r')
Lines = file1.readlines()
for line in Lines:
    if line.startswith('$ cd /'):
        currentDir = fs
    elif line.startswith("$ cd .."):
        currentDir = currentDir[".."]
    elif line.startswith("$ ls"):
        i = 0 #noop
    elif line.startswith("$ cd"):
        folderName = line.split(' ')[2]
        currentDir = currentDir[folderName]
    elif line.startswith("dir "):
        folderName = line.split(' ')[1]
        subDir = {}
        subDir[".."]=currentDir
        currentDir[folderName] = subDir
    else:
        parts=line.split(' ')
        fileSize = int(parts[0])
        fileName = parts[1]
        currentDir[fileName] = fileSize

#pretty(fs)

print("fs size: " + str(calcSize(fs)))
print("large dicts sum: " + str(sum(largeDicts)))