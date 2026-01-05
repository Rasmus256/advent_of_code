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
        if len(s) % 2 == 0:
            mid = len(s) // 2
            if s[:mid] == s[mid:]:
                result += i
                print(i)
    
print(result)
