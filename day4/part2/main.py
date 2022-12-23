file1 = open('puzzle_input.csv', 'r')

def fullyContains(first, second):
  startBeforeOtherStart = int(first[0].strip()) <= int(second[0].strip())
  endAfterOtherEnd = int(first[1].strip()) >= int(second[1].strip())
  startWithinOtherRange = int(first[0].strip()) >= int(second[0].strip()) and int(first[0].strip()) <= int(second[1].strip())
  endWithinOtherRange = int(first[1].strip()) >= int(second[0].strip()) and int(first[1].strip()) <= int(second[1].strip())

  return (startBeforeOtherStart and (endAfterOtherEnd or endWithinOtherRange)) or (startWithinOtherRange and (endAfterOtherEnd or endWithinOtherRange))

Lines = file1.readlines()
fullycontainedElements = 0
for line in Lines:
    parts = line.split(',')
    limits1 = parts[0].split('-')
    limits2 = parts[1].split('-')
    if fullyContains(limits1, limits2) and fullyContains(limits2, limits1):
      fullycontainedElements = fullycontainedElements+1

print(fullycontainedElements)