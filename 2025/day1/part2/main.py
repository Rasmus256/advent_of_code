with open('puzzle_input.csv', 'r') as file:
    lines = file.readlines()

position = 50
result = 0

for line in lines:
    direction, steps = line.strip()[0], int(line.strip()[1:])
    
    # Calculate threshold: the number of steps needed to first reach 0
    if direction == "R":
        threshold = (100 - position) % 100 or 100
    else:  # Left
        threshold = position or 100
    
    # Count how many times we pass through 0:
    # - Every 100 steps crosses 0 once
    # - Plus 1 if the remaining steps reach the threshold
    result += (steps // 100) + (1 if steps % 100 >= threshold else 0)
    
    # Update position
    position = (position + (steps if direction == "R" else -steps)) % 100

print(result)
