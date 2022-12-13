file1 = open('puzzle_input.csv', 'r')

def characterToInt(ch):
  if ch.isupper():
    return ord(ch)-65+27
  if ch.islower():
    return ord(ch)-97+1

Lines = file1.readlines()
priorities = []
commonElemnent = ''
for line in Lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    i = list(set(firstpart).intersection(secondpart))
    if len(i) > 1:
        raise NotImplementedError
    priorities.append(characterToInt(i[0]))

print(priorities)
print(sum(priorities))