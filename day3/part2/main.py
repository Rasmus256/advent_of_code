file1 = open('puzzle_input.csv', 'r')

def characterToInt(ch):
  if ch.isupper():
    return ord(ch)-65+27
  if ch.islower():
    return ord(ch)-97+1

def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

Lines = file1.readlines()
priorities = []
commonElemnent = ''
for linechunk in divide_chunks(Lines,3):
    line1, line2, line3 = linechunk[0].strip(), linechunk[1].strip(), linechunk[2].strip()
    i = list(set(line1).intersection(line2).intersection(line3))
    if len(i) > 1:
        raise NotImplementedError
    priorities.append(characterToInt(i[0]))

print(sum(priorities))