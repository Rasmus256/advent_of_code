
from typing import List, Tuple


def _pad_grid(grid_lines: List[str]) -> List[str]:
	width = max(len(l) for l in grid_lines)
	return [l.ljust(width) for l in grid_lines]


def _find_column_runs(padded: List[str]) -> List[Tuple[int, int]]:
	width = len(padded[0])
	occupied = [any(row[col] != ' ' for row in padded) for col in range(width)]
	runs: List[Tuple[int, int]] = []
	start = None
	for i, occ in enumerate(occupied):
		if occ and start is None:
			start = i
		elif not occ and start is not None:
			runs.append((start, i))
			start = None
	if start is not None:
		runs.append((start, width))
	return runs


def read_problems(path: str) -> List[Tuple[List[int], str]]:
	"""Parse the input file into problems.

	The file is expected to contain a small grid of characters on the first N-1 lines
	representing numbers laid out in columns; the last line contains the operand
	tokens (one per problem). Each problem occupies a contiguous run of character
	columns; for each column in a run we read top->down to build a number token.

	If the column-run detection doesn't produce the same count as operand tokens,
	a fallback token-splitting method is attempted (split each number-line on
	whitespace and transpose).
	"""
	with open(path, 'r') as fh:
		lines = [line.rstrip('\n') for line in fh]
		if not lines:
			return []
		operand_tokens = lines[-1].strip().split()
		grid_lines = lines[:-1]
		if not grid_lines:
			return []
		padded = _pad_grid(grid_lines)
		runs = _find_column_runs(padded)
		# if runs and operands mismatch, fallback to whitespace-token parsing
		if len(runs) != len(operand_tokens):
			# try original token-splitting approach: split each number-line and transpose
			digit_rows = [l.strip().split() for l in grid_lines]
			try:
				columns = list(zip(*digit_rows))
			except Exception:
				columns = []
			result: List[Tuple[List[int], str]] = []
			for col_tokens, operand in zip(columns, operand_tokens):
				result.append(([int(tok) for tok in col_tokens], operand))
			return result

		result: List[Tuple[List[int], str]] = []
		for (s, e), operand in zip(runs, operand_tokens):
			digits: List[int] = []
			for col in range(s, e):
				tok = ''.join(row[col] for row in padded).strip()
				if not tok:
					continue
				digits.append(int(tok))
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
