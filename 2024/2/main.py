"""Solution for https://adventofcode.com/2024/day/2."""

import logging
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_variants(report: List[int]) -> List[List[int]]:
    """Get all variants of a list where a single element is removed."""
    return [report[:i] + report[i + 1 :] for i in range(len(report))]


def is_safe_report(report: List[int]) -> bool:
    """
    Return True if report is safe, else False.

    It is safe if all differences between the numbers in the report  have the same sign and if
    the differences are larger or equal to 1 and smaller or equal to 3.
    """
    diffs = [report[index] - report[index - 1] for index in range(1, len(report))]
    same_sign = all([diff > 0 for diff in diffs] if diffs[0] > 0 else [diff < 0 for diff in diffs])
    diffs_within_range = all([3 >= abs(diff) >= 1 for diff in diffs])
    return same_sign and diffs_within_range


if __name__ == "__main__":
    with open("input.txt") as f:
        reports = [list(map(int, line.strip().split())) for line in f.readlines()]

    part1 = sum(is_safe_report(report) for report in reports)
    part2 = sum(
        1 for report in reports if any(is_safe_report(variant) for variant in get_variants(report))
    )

    logger.info("Advent of Code 2024 | Day 2")
    logger.info(f"Answer part 1: {part1}")
    logger.info(f"Answer part 2: {part2}")
