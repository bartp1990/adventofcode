import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    tmp_grid = []
    for i_row, line in enumerate(lines):
        row = []
        for i_col, char in enumerate(list(line.strip())):
            row.append(char)

        tmp_grid.append(row)

    grid = np.array(tmp_grid)
    shape = grid.shape

    visited = set()

    def find_region(coord, char):
        area = 0
        perimeter = 0

        stack = [coord]

        while stack:
            current_coord = stack.pop()
            if current_coord in visited:
                continue
            visited.add(current_coord)
            area += 1
            neighbours = [
                (current_coord[0] - 1, current_coord[1]),  # Up
                (current_coord[0] + 1, current_coord[1]),  # Down
                (current_coord[0], current_coord[1] - 1),  # Left
                (current_coord[0], current_coord[1] + 1),  # Right
            ]

            for n_coord in neighbours:
                if 0 <= n_coord[0] < shape[0] and 0 <= n_coord[1] < shape[1]:
                    if grid[n_coord[0], n_coord[1]] == char and n_coord not in visited:
                        stack.append(n_coord)
                    elif grid[n_coord[0], n_coord[1]] != char:
                        perimeter += 1
                else:
                    perimeter += 1
        return area, perimeter

    regions = []

    for y in range(0, shape[0]):
        for x in range(0, shape[1]):
            coord = (x, y)
            if coord not in visited:
                char = grid[coord[0], coord[1]]
                area, perimeter = find_region(coord, char)
                regions.append({"char": char, "area": area, "perimeter": perimeter})

    for region in regions:
        logger.info(f"Region: Char = {region['char']}, Area = {region['area']}, Perimeter = {region['perimeter']}")

    print(sum(region['area'] * region['perimeter'] for region in regions))
