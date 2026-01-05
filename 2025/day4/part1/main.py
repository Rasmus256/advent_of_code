from itertools import product


def count_low_adjacent_batteries(path: str) -> int:
	"""Return the count of '@' cells that have fewer than 4 adjacent '@' neighbors.

	Reads a spatial grid from `path`. The function is explicit about intent and
	uses generator expressions + enumerate for clarity.
	"""
	with open(path, 'r') as fh:
		grid = [list(line.rstrip('\n')) for line in fh]

	rows = len(grid)
	neighbor_offsets = [
		(dr, dc) for dr, dc in product((-1, 0, 1), repeat=2) if not (dr == 0 and dc == 0)
	]

	total = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch != '@':
				continue

			adjacent = sum(
				1
				for row_offset, col_offset in neighbor_offsets
				if 0 <= (nr := r + row_offset) < rows
				and 0 <= (nc := c + col_offset) < len(grid[nr])
				and grid[nr][nc] == '@'
			)

			if adjacent < 4:
				total += 1

	return total


if __name__ == '__main__':
	result = count_low_adjacent_batteries('puzzle_input.csv')
	print(result)
