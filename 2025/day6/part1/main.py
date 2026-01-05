from itertools import product


def read_problems(path: str):
	"""Read the input file and return the list of problems. each problem consists of a number of digits and an operand
	"""
	with open(path, 'r') as fh:
		lines = []
		for line in fh:
			line = line.lstrip()
			line.split()
			lines.append(line)
		operand_line = lines[-1].split()
		digit_lines = [l.split() for l in lines[:-1]]
		print(operand_line)
		print(digit_lines)
		result = []
		for problem_index in range(len(operand_line)):
			print(problem_index)
			digits = []
			for digit_line in digit_lines:
				digits.append(int(digit_line[problem_index]))
			operand = operand_line[problem_index]
			result.append((digits, operand))
	return result

if __name__ == '__main__':
	problems = read_problems('puzzle_input.csv')
	total = 0
	for (digits, operand) in problems:
		if operand == '+':
			result = sum(digits)
		elif operand == '*':
			result = 1
			for d in digits:
				result *= d
		print( result)
		total += result
	print(f'Total: {total}')
