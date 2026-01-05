from itertools import product
from typing import List, Tuple


def find_cells_to_remove(grid: List[List[str]], neighbor_offsets: List[Tuple[int, int]]) -> Tuple[int, List[Tuple[int, int]]]:
   """Return (count, cells_to_remove) for current grid state.

   A cell is removable if it contains '@' and has fewer than 4 adjacent '@' neighbors.
   """
   rows = len(grid)
   cells_to_remove: List[Tuple[int, int]] = []
   count = 0

   for r, row in enumerate(grid):
      for c, ch in enumerate(row):
         if ch != '@':
            continue

         adjacent = sum(
            1
            for row_off, col_off in neighbor_offsets
            if 0 <= (nr := r + row_off) < rows
            and 0 <= (nc := c + col_off) < len(grid[nr])
            and grid[nr][nc] == '@'
         )

         if adjacent < 4:
            cells_to_remove.append((r, c))
            count += 1

   return count, cells_to_remove


def process_grid(path: str) -> int:
   """Load grid from `path`, iteratively remove weak cells, and return total removed count."""
   with open(path, 'r') as fh:
      grid = [list(line.rstrip('\n')) for line in fh]

   neighbor_offsets = [
      (dr, dc) for dr, dc in product((-1, 0, 1), repeat=2) if not (dr == 0 and dc == 0)
   ]

   total_removed = 0
   count, cells_to_remove = find_cells_to_remove(grid, neighbor_offsets)
   total_removed += count

   while cells_to_remove:
      for r, c in cells_to_remove:
         grid[r][c] = '.'
      count, cells_to_remove = find_cells_to_remove(grid, neighbor_offsets)
      total_removed += count

   return total_removed


if __name__ == '__main__':
   result = process_grid('puzzle_input.csv')
   print(result)
