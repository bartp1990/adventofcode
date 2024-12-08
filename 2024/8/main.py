"""Solution for https://adventofcode.com/2024/day/8."""

import itertools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_anti_nodes_part1():
    anti_nodes = set()
    for _, coords in pos_per_type.items():
        permutations = set(itertools.permutations(coords, 2))
        for p in permutations:
            new_pos_y = p[0][0] - (p[0][0] - p[1][0]) * 2
            new_pos_x = p[0][1] - (p[0][1] - p[1][1]) * 2
            if max_y < new_pos_y or new_pos_y < 0 or max_x < new_pos_x or new_pos_x < 0:
                continue
            anti_nodes.add((new_pos_y, new_pos_x))

    return len(anti_nodes)


def get_anti_nodes_part2():
    anti_nodes = set()
    for _, coords in pos_per_type.items():
        combinations = set(itertools.combinations(coords, 2))

        for c in combinations:
            first = c[0]
            dy = c[0][0] - c[1][0]
            dx = c[0][1] - c[1][1]

            for i in range(-max_x, max_x):
                y = first[0] - dy * i
                x = first[1] - dx * i

                if max_y < y or y < 0 or max_x < x or x < 0:
                    continue

                anti_nodes.add((y, x))

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
                if char not in pos_per_type:
                    pos_per_type[char] = set()

                coord = (y, x)
                pos_per_type[char].add(coord)

    part_1 = get_anti_nodes_part1()
    part_2 = get_anti_nodes_part2()

    logger.info("Advent of Code 2024 | Day 8")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
