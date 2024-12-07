"""Solution for https://adventofcode.com/2024/day/5."""

import logging
import itertools
from functools import lru_cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

OPERATIONS_PART_1 = ("+", "*")
OPERATIONS_PART_2 = ("+", "*", "||")

def solve(calc):
    while len(calc) != 1:
        if calc[1] == "+":
            calc[0] = calc[0] + calc[2]
        elif calc[1] == "*":
            calc[0] = calc[0] * calc[2]
        elif calc[1] == "||":
            calc[0] = int(f"{calc[0]}{calc[2]}")

        del calc[1:3]

    return calc[0]

@lru_cache
def get_permutations(operations, length):
    return list(itertools.product(operations, repeat=length - 1))

def calculate(operations, problem_set) -> int:
    final_answer = 0
    for answer, numbers in problem_set.items():
        permutations = get_permutations(operations, len(numbers))

        for permutation in permutations:
            expression = list(itertools.chain(*itertools.zip_longest(numbers, permutation)))
            del expression[-1]
            result = solve(expression)

            if result == answer:
                final_answer += answer
                break

    return final_answer


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    split_lines = [line.split(":") for line in lines]
    problems = {int(line[0]): list(map(int, line[1].split())) for line in split_lines}

    part_1 = calculate(OPERATIONS_PART_1, problems)
    part_2 = calculate(OPERATIONS_PART_2, problems)

    logger.info("Advent of Code 2024 | Day 5")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
