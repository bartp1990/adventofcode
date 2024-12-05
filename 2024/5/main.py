"""Solution for https://adventofcode.com/2024/day/5."""

import logging
from functools import cmp_to_key

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()

    rules, numbers = lines.split("\n\n")
    updates = [list(map(int, num_list.split(","))) for num_list in numbers.split("\n")]

    def compare(x: int, y: int):
        """If a ruleset exists for the two numbers sort x before y, else don't."""
        return -1 if f"{x}|{y}" in rules else 0

    totals = {"correct": 0, "incorrect": 0}
    for update_sequence in updates:
        corrected = sorted(update_sequence, key=cmp_to_key(compare))
        index = "correct" if corrected == update_sequence else "incorrect"
        totals[index] += corrected[len(corrected) // 2]

    part_1, part_2 = totals.values()

    logger.info("Advent of Code 2024 | Day 5")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
