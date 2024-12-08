"""Solution for https://adventofcode.com/2024/day/8."""

import logging
import itertools
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    pos_per_type = dict()
    anti_nodes = set()

    max_y = len(lines) - 1
    max_x = len(list(lines[0].strip())) - 1

    for y, line in enumerate(lines):
        for x, char in enumerate(list(line.strip())):
            if char != ".":
                if not char in pos_per_type:
                    pos_per_type[char] = set()

                coord = (y, x)
                pos_per_type[char].add(coord)

    for _, coords in pos_per_type.items():
        permutations = set(itertools.permutations(coords, 2))
        for per in permutations:

            for i in range(1, 2):
                diff_y = per[0][0] - per[1][0] * i
                diff_x = per[0][1] - per[1][1] * i

                new_pos_y = per[1][0] - diff_y
                new_pos_x = per[1][1] - diff_x

                if max_y < new_pos_y or new_pos_y < 0 or max_x < new_pos_x or new_pos_x < 0:
                    continue

                new_pos = (new_pos_y, new_pos_x)

                if new_pos not in anti_nodes:
                    anti_nodes.add(new_pos)

    # grid = np.full((max_y+1, max_x+1), ".")
    # for t, coords in pos_per_type.items():
    #     for coord in coords:
    #         grid[*coord] = t
    #
    # for row in grid:
    #     print(''.join(map(str, row)))

    part_1 = len(anti_nodes)
    part_2 = None

    logger.info("Advent of Code 2024 | Day 8")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
