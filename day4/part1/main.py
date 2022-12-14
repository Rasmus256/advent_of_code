file1 = open('puzzle_input.csv', 'r')

def fullyContains(first, second):
  ret1 = int(first[0].strip()) <= int(second[0].strip())
  ret2 = int(first[1].strip()) >= int(second[1].strip())
  print(ret1)
  print(ret2)
  return ret1 and ret2

Lines = file1.readlines()
fullycontainedElements = 0
for line in Lines:
    print(line)
    parts = line.split(',')
    print(parts)
    limits1 = parts[0].split('-')
    print(limits1)
    limits2 = parts[1].split('-')
    print(limits2)
    if fullyContains(limits1, limits2) or fullyContains(limits2, limits1):
      fullycontainedElements = fullycontainedElements+1

print(fullycontainedElements)