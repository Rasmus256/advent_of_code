with open('puzzle_input.csv', 'r') as file:
    lines = file.readlines()

position = 50
result = 0

for line in lines:
    direction, steps = line.strip()[0], int(line.strip()[1:])
    position += steps if direction == "R" else -steps
    position %= 100
    
    if position == 0:
        result += 1

print(result)
