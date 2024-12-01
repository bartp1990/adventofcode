"""Solution for day 1: https://adventofcode.com/2024/day/1."""

from collections import Counter
from pathlib import Path
from typing import List, Tuple


def get_problem_input(path: Path):
    """Parse the input file and divide the input into two lists."""
    with open(path) as f:
        location_ids = [list(map(int, line.strip().split())) for line in f.readlines()]
    return [id[0] for id in location_ids], [id[1] for id in location_ids]


def get_answers(list1: List[int], list2: List[int]) -> Tuple[int, int]:
    """
    Return problem answers as ints given two lists of int as input.

    For part1, sort the lists, and then take the absolute value of the difference for each pair and
    sum them all together.
    For part2, use the counter object to quickly count each occurrence and calculate the score.
    """
    part1 = sum([abs(first - second) for first, second in zip(sorted(list1), sorted(list2))])
    count = Counter(list2)
    part2 = sum([count[number] * number for number in list1 if number in count])
    return part1, part2


if __name__ == "__main__":
    list1, list2 = get_problem_input(Path("input"))
    part1, part2 = get_answers(list1, list2)
    print("Advent of Code 2024 | Day 1")
    print(f"Answer part 1: {part1}")
    print(f"Answer part 2: {part2}")
