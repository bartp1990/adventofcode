"""Solution for https://adventofcode.com/2024/day/8."""

import logging
import itertools
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def print_grid(anti_nodes):
    grid = np.full((max_y+1, max_x+1), ".")
    for coord in anti_nodes:
        grid[*coord] = "#"

    for row in grid:
        print(''.join(map(str, row)))

    print("\n")

def get_anti_nodes(include_antennas):
    anti_nodes = set()
    for _, coords in pos_per_type.items():
        permutations = set(itertools.permutations(coords, 2))

        for p in permutations:
            for i in range(1, 2):
                new_pos_y = p[0][0] - (p[0][0] - p[1][0]) * i * 2
                new_pos_x = p[0][1] - (p[0][1] - p[1][1]) * i * 2

                if max_y < new_pos_y or new_pos_y < 0 or max_x < new_pos_x or new_pos_x < 0:
                    continue

                anti_nodes.add((new_pos_y, new_pos_x))


    print_grid(anti_nodes)
    return len(anti_nodes)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    pos_per_type = dict()
    max_y = len(lines) - 1
    max_x = len(list(lines[0].strip())) - 1

    for y, line in enumerate(lines):
        for x, char in enumerate(list(line.strip())):
            if char != ".":
                if not char in pos_per_type:
                    pos_per_type[char] = set()

                coord = (y, x)
                pos_per_type[char].add(coord)

    part_1 = get_anti_nodes(include_antennas=False)

    logger.info("Advent of Code 2024 | Day 8")
    logger.info(f"Answer part 1: {part_1}")
    # logger.info(f"Answer part 2: {part_2}")