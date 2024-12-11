"""Solution for https://adventofcode.com/2024/day/11."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

import math

blink_cache = dict()
leaf_nodes = []

def split_number(n, num_digits):
    n = abs(n)  # Ensure the number is positive
    split_point = num_digits // 2
    divisor = 10 ** split_point
    first = n // divisor
    second = n % divisor
    return first, second

def is_even_number_of_digits(n, num_digits):
    if n == 0:
        return True  # 0 has 1 digit, so it's odd, but we can treat it as even if preferred
    return num_digits % 2 == 0

def blink(n: int, cur_it, num_iterations, total):
    if n in blink_cache:
        result = blink_cache[n]
    else:
        num_digits = math.floor(math.log10(n)) + 1 if n > 0 else 0
        if n == 0:
            result = 1
        elif is_even_number_of_digits(n, num_digits):
            result = split_number(n, num_digits)
        else:
            result = n * 2024

        if cur_it < num_iterations:
            if isinstance(result, tuple):
                for r in result:
                    result, total = blink(r, cur_it + 1, num_iterations, total)
            else:
                result, total = blink(result, cur_it + 1, num_iterations, total)

        blink_cache[n] = result

    # Only count leaf nodes here (final step in the recursion)
    leaf_nodes = globals()["leaf_nodes"]
    leaf_nodes.append(result)

    return result, total

if __name__ == "__main__":
    with open("input.txt") as f:
        stones = list(map(int, f.read().split()))

        part_1 = 0
        for stone in stones:
            _, total = blink(stone, 1, 75, 0)
            part_1 += total



    logger.info("Advent of Code 2024 | Day 11")
    logger.info(f"Answer part 1: {len(leaf_nodes)}")
    # logger.info(f"Answer part 2: {part_2}")
