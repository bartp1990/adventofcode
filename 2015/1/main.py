"""Solution for https://adventofcode.com/2015/1."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.read()

    char_map = {
        "(": 1,
        ")": -1,
    }

    part1 = sum([char_map[c] for c in file])

    part2 = None
    floor = 0
    for i, c in enumerate(file):
        floor += char_map[c]
        if floor == -1:
            part2 = i + 1
            break

    logger.info("Advent of Code 2015 | Day 1")
    logger.info(f"Answer part 1: {part1}")
    logger.info(f"Answer part 2: {part2}")
