from itertools import product


def read_database(path: str):
	"""Read the input file and return the list of fresh ingredient ranges and the list of available ingredient ids.
	Each fresh ingredient range is returned as a tuple `(start, end)` where `end` is exclusive.
	"""
	with open(path, 'r') as fh:
		doing_ingredient_list = True
		fresh_ingredients = []
		available_ingredients = []
		for line in fh:
			line = line.strip()
			if line == '':
				doing_ingredient_list = False
				continue
			if doing_ingredient_list:
				start, end = line.split('-')
				fresh_ingredients.append((int(start), int(end) + 1))
			else:
				available_ingredients.append(int(line))
	return fresh_ingredients, available_ingredients


if __name__ == '__main__':
	fresh_ingredients, available_ingredients = read_database('puzzle_input.csv')
	# sort fresh ingredient ranges by their start index
	fresh_ingredients.sort(key=lambda r: r[0])
	# merge overlapping/adjacent fresh ranges and compute unique count without expanding elements
	merged = []
	for start, end in fresh_ingredients:
		if not merged or start > merged[-1][1]:
			merged.append([start, end])
		else:
			merged[-1][1] = max(merged[-1][1], end)

	unique_count = sum(r[1] - r[0] for r in merged)

	print(f'Count Fresh ingredients: {unique_count}')
