import logging
import re
from dataclasses import dataclass, field
from idlelib.debugger_r import gui_adap_oid

import numpy as np
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SIZE_X = 101
SIZE_Y = 103

def print_grid(grid: np.ndarray):
    for row in grid:
        row = np.array(["." if c == 0 else c for c in row])
        print("".join(list(map(str, row))))
    print("\n")

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


    def security_score(self, t):
        g = self.grid_at_time(t=t)
        quad_width = g.shape[1] // 2
        quad_height = g.shape[0] // 2
        print(g.shape)
        quarters = (
            g[0 : quad_height, 0 : quad_width: ],
            g[0 : quad_height, quad_width +1: ],
            g[quad_height+1:, 0 : quad_width],
            g[quad_height+1:, quad_width+1:],
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

    grid.print(t=100)
    part_1 = grid.security_score(t=100)

    part_2 = None

    logger.info("Advent of Code 2024 | Day 1")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
