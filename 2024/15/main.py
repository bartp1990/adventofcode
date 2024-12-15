import logging

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def print_grid(grid: np.ndarray):
    for row in grid:
        row = np.array(["." if c == 0 else c for c in row])
        print("".join(list(map(str, row))))
    print("\n")


class Grid:
    def __init__(self, lines):
        self.grid = np.full((len(lines), len(lines[0])), ".")
        for y, line in enumerate(lines):
            for x, char in enumerate(list(line)):
                self.grid[x, y] = char
                if char == "@":
                    self.robot_pos = (x, y)

    def print(self):
        result = ""
        for y in range(0, self.grid.shape[1]):
            for x in range(0, self.grid.shape[0]):
                result += self.grid[x, y]
            result += "\n"
        result += "\n"
        print(result)


if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.read()

    grid, instructions = file.split("\n\n")
    grid = grid.split("\n")
    instructions = list(instructions)
    grid = Grid(grid)

    part_1 = None
    part_2 = None

    logger.info("Advent of Code 2024 | Day 15")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
