file1 = open('puzzle_input.csv', 'r')
 
Lines = file1.readlines()
result = 0
ranges = []
Lines[0] = Lines[0].removesuffix("\n")
Lines = Lines[0].split(",")
for rangeText in Lines:
    rangeLimits = rangeText.split("-")
    ranges.append([rangeLimits[0], rangeLimits[1]])
for r in ranges:
    rangeStart = int(r[0])
    rangeEnd = int(r[1])
    for i in range(rangeStart, rangeEnd + 1):
        s = str(i)
        n = len(s)
        found = False
        for p in range(1, n // 2 + 1):
            if n % p != 0:
                continue
            if s == s[:p] * (n // p):
                found = True
                break
        if found:
            result += i
    
print(result)
