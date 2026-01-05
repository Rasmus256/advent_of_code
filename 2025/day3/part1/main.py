def max_joltage(batteries, num_digits):
    """Greedy approach: select num_digits to form the largest number while maintaining order."""
    result_str = ""
    start_idx = 0
    
    for pos in range(num_digits):
        remaining_needed = num_digits - pos - 1
        max_idx = len(batteries) - remaining_needed - 1
        
        # Find the largest digit in the valid range
        best_idx = max(range(start_idx, max_idx + 1), key=lambda i: batteries[i])
        result_str += str(batteries[best_idx])
        start_idx = best_idx + 1
    
    return int(result_str)


file1 = open('puzzle_input.csv', 'r')
Lines = file1.readlines()
result = 0

for batteryBank in Lines:
    batteries = [int(d) for d in batteryBank.strip() if d.isdigit()]
    result += max_joltage(batteries, 2)
    
print(result)
