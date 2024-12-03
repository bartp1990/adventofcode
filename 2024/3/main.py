"""Solution for https://adventofcode.com/2024/day/3."""

import logging
import math
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.read()

    def get_mul_product(text: str) -> int:
        """Extract all pairs of mul(x,y) digits and return the sum of their products."""
        all_mul_pairs = r"mul\((\d+),\s*(\d+)\)"
        matches = re.findall(all_mul_pairs, text)
        return sum([math.prod(list(map(int, match))) for match in matches])

    part1 = get_mul_product(file)

    only_text_outside_dont_do = r"(?s)(?<=^|(?<=\bdo\(\)))((?:(?!don\'t\(\)).)*)"
    valid_instructions = re.findall(only_text_outside_dont_do, file)
    part2 = get_mul_product("".join(valid_instructions))

    logger.info("Advent of Code 2024 | Day 3")
    logger.info(f"Answer part 1: {part1}")
    logger.info(f"Answer part 2: {part2}")
