"""Solution for https://adventofcode.com/2024/day/5."""

import logging
import itertools

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

OPERATIONS_PART_1 = ["+", "*"]
OPERATIONS_PART_2 = ["+", "*", "||"]

def apply_concat(expression):
    joint_expression = " ".join(expression)
    joint_expression = joint_expression.replace(" || ", "")
    result = joint_expression.split()
    return result


def solve(calc):
    while len(calc) != 1:
        if calc[1] == "+":
            calc = [int(calc[0]) + int(calc[2]), *calc[3:]]
        elif calc[1] == "*":
            calc = [int(calc[0]) * int(calc[2]), *calc[3:]]
        elif calc[1] == "||":
            calc = [int(str(calc[0]) + str(calc[2])), *calc[3:]]

    return int(calc[0])

def calculate(operations, problem_set ) -> int:
    final_answer = 0
    for answer, numbers in problem_set.items():
        permutations = list(itertools.product(operations, repeat=len(numbers) - 1))

        for permutation in permutations:
            expression = list(itertools.chain(*itertools.zip_longest(numbers, permutation)))
            expression = list(filter(lambda x: x is not None, expression.copy()))
            result = solve(expression.copy())

            if result == int(answer):
                final_answer += int(answer)
                break

    return final_answer


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    split_lines = [line.split(":") for line in lines]
    problems = {line[0]: line[1].split() for line in split_lines}

    part_1 = calculate(OPERATIONS_PART_1, problems)
    part_2 = calculate(OPERATIONS_PART_2, problems)

    logger.info("Advent of Code 2024 | Day 5")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
