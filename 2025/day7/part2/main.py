from itertools import product


def read_problems(path: str):
	"""Read the input file and return a list of indeces that contain either 'S' or '^'
	   Ignore lines containing only '.'.
	"""
	result = []
	with open(path, 'r') as fh:
		for line in fh:
			indeces = [i for i, c in enumerate(line) if c == 'S' or c == '^']
			if indeces:
				result.append(indeces)
	print(result)
	return result

if __name__ == '__main__':
	problems = read_problems('puzzle_input.csv')
	tachyons = [problems[0][0]]
	total = 1
	for splitterline in problems[1:]:
		new_tachyons = []
		count_before= len(tachyons)
		for tachyon in tachyons:
			if tachyon in splitterline:
				new_tachyons.append(tachyon-1)
				new_tachyons.append(tachyon+1)
				total *= 2
			else:
				new_tachyons.append(tachyon)
		tachyons = set(new_tachyons)
		print(set(new_tachyons))
	print("Total:", total)