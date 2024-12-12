"""Solution for https://adventofcode.com/2024/day/11."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

import math
from functools import cache
NUM_ITERATIONS = 75

@cache
def split_number(n, num_digits):
    n = abs(n)  # Ensure the number is positive
    split_point = num_digits // 2
    divisor = 10 ** split_point
    first = n // divisor
    second = n % divisor
    return first, second

def is_even_number_of_digits(n, num_digits):
    if n == 0:
        return True
    return num_digits % 2 == 0

@cache
def blink(n: int, cur_it):

    if cur_it == NUM_ITERATIONS:
        return 1

    num_digits = math.floor(math.log10(n)) + 1 if n > 0 else 0
    if n == 0:
        return blink(1, cur_it+1)
    elif is_even_number_of_digits(n, num_digits):
        first, second = split_number(n, num_digits)
        return blink(first, cur_it+1) + blink(second, cur_it+1)
    else:
        return blink(n * 2024, cur_it+1)

if __name__ == "__main__":
    with open("input.txt") as f:
        stones = list(map(int, f.read().split()))

        part_2 = 0
        for stone in stones:
            part_2 += blink(stone, 0)

    logger.info("Advent of Code 2024 | Day 11")
    logger.info(f"Answer part 2: {part_2}")