file1 = open('puzzle_input.csv', 'r')

Lines = file1.readlines()
counters = []
count = 0
for line in Lines:
    if line != "\n":
        count += int(line.strip())
    else:
        counters.append(count)
        count=0

counters.sort(reverse=True)
print(sum(counters[:3]))
