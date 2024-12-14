import logging
import re
from dataclasses import dataclass, field
import numpy as np
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SIZE_X = 11
SIZE_Y = 7


@dataclass
class Robot:
    pos: np.array
    velocity: np.array

    def position_at_time(self, t):
        new_pos = self.pos + self.velocity * t
        wrapped_pos = np.mod(new_pos, [SIZE_Y, SIZE_X])
        return wrapped_pos


@dataclass
class Grid:
    grid: np.ndarray = field(default_factory=lambda: np.array([]))
    robots: List[Robot] = field(default_factory=list)

    def __post_init__(self):
        # Initialize arr with a size x size matrix filled with 0
        self.arr = np.zeros((SIZE_Y, SIZE_X))

    def grid_at_time(self, t):
        grid_at_t = np.full((SIZE_Y, SIZE_X), 0, dtype=int)
        for robot in self.robots:
            pos = robot.position_at_time(t=t)
            grid_at_t[pos[0], pos[1]] += 1

        return grid_at_t

    def print(self, t):
        printed_grid = self.grid_at_time(t=t)
        for row in printed_grid:
            row = np.array(["." if c == 0 else c for c in row])
            print("".join(list(map(str, row))))
        print("\n")

    def security_score(self, t):
        g = self.grid_at_time(t=t)
        quarters = (
            g[0 : g.shape[0] // 2, 0 : g.shape[1] // 2],
            g[0 : g.shape[0] // 2, (g.shape[1] // 2 + 1):],
            g[(g.shape[1] // 2) -1:, 0 : g.shape[1] // 2],
            g[(g.shape[1] // 2) -1:, (g.shape[1] // 2) +1:],
        )

        sums = [np.sum(q) for q in quarters]
        print(sums)
        return np.prod(sums)


if __name__ == "__main__":  # Default empty array, will be overwritten
    with open("input.txt") as f:
        lines = f.readlines()

    grid = Grid()

    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        match = re.match(pattern, line)
        x, y, vx, vy = list(map(int, [i for i in match.groups()]))
        grid.robots.append(Robot(np.array([y, x]), np.array([vy, vx])))

    part_1 = grid.security_score(t=100)
    grid.print(t=100)
    part_2 = None

    logger.info("Advent of Code 2024 | Day 1")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
