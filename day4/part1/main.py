file1 = open('puzzle_input.csv', 'r')

def fullyContains(first, second):
  startBeforeOtherStart = int(first[0].strip()) <= int(second[0].strip())
  endAfterOtherEnd = int(first[1].strip()) >= int(second[1].strip())
  startWithinOtherRange = int(first[0].strip()) >= int(second[0].strip()) and int(first[0].strip()) <= int(second[1].strip())
  endWithinOtherRange = int(first[1].strip()) >= int(second[0].strip()) and int(first[1].strip()) <= int(second[1].strip())
  print(startBeforeOtherStart)
  print(endAfterOtherEnd)
  print(startWithinOtherRange)
  print(endWithinOtherRange)
  return startBeforeOtherStart or endAfterOtherEnd or startWithinOtherRange or endWithinOtherRange

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