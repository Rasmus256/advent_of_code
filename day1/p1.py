file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
count = 0
currentMax = 0
for line in Lines:
    if line != "\n":
        count += int(line.strip())
    else:
        currentMax = max(currentMax, count)
        count=0
print(currentMax)

