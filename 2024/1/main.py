"""Solution for https://adventofcode.com/2024/day/1."""

import logging
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        location_ids = [list(map(int, line.strip().split())) for line in f.readlines()]

    list1, list2 = [loc[0] for loc in location_ids], [loc[1] for loc in location_ids]

    part1 = sum([abs(first - second) for first, second in zip(sorted(list1), sorted(list2))])

    count = Counter(list2)
    part2 = sum([count[number] * number for number in list1 if number in count])

    logger.info("Advent of Code 2024 | Day 1")
    logger.info(f"Answer part 1: {part1}")
    logger.info(f"Answer part 2: {part2}")
