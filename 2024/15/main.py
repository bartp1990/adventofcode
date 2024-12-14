import logging
import re
from dataclasses import dataclass, field

import numpy as np
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def print_grid(grid: np.ndarray):
    for row in grid:
        row = np.array(["." if c == 0 else c for c in row])
        print("".join(list(map(str, row))))
    print("\n")




if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    part_1 = None
    part_2 = None

    logger.info("Advent of Code 2024 | Day 15")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
