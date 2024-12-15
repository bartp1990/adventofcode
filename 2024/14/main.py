import logging
import re
from dataclasses import dataclass, field
from typing import List

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SIZE_X = 101
SIZE_Y = 103


def print_grid(grid: np.ndarray):
    for row in grid:
        row = np.array(["." if c == 0 else c for c in row])
        print("".join(list(map(str, row))))
    print("\n")


def density_score(arr):
    rows, cols = arr.shape
    filled_count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            top = arr[i - 1, j]
            bottom = arr[i + 1, j]
            left = arr[i, j - 1]
            right = arr[i, j + 1]

            if top >= 1 and bottom >= 1 and left >= 1 and right >= 1:
                filled_count += 1

    return filled_count


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

    def grid_at_time(self, t):
        grid_at_t = np.full((SIZE_Y, SIZE_X), 0, dtype=int)
        for robot in self.robots:
            pos = robot.position_at_time(t=t)
            grid_at_t[pos[0], pos[1]] += 1

        return grid_at_t

    def security_score(self, t):
        g = self.grid_at_time(t=t)
        quad_width = g.shape[1] // 2
        quad_height = g.shape[0] // 2
        print(g.shape)
        quarters = (
            g[0:quad_height, 0:quad_width:],
            g[0:quad_height, quad_width + 1 :],
            g[quad_height + 1 :, 0:quad_width],
            g[quad_height + 1 :, quad_width + 1 :],
        )

        sums = [np.sum(q) for q in quarters]
        print(sums)
        return np.prod(sums)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    grid = Grid()

    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        match = re.match(pattern, line)
        x, y, vx, vy = list(map(int, [i for i in match.groups()]))
        grid.robots.append(Robot(np.array([y, x]), np.array([vy, vx])))

    part_1 = grid.security_score(t=100)

    highest_density = 0
    highest_density_t = 0
    for i in range(0, 10000):
        d = density_score(grid.grid_at_time(t=i))
        print(i, d)

        if d > highest_density:
            highest_density = d
            highest_density_t = i

    part_2 = highest_density_t

    import matplotlib.pyplot as plt
    import numpy as np

    def convert_to_bw_image(arr):
        bw_image = np.where(arr >= 1, 255, 0).astype(np.uint8)
        return bw_image

    bw_image = convert_to_bw_image(grid.grid_at_time(t=highest_density_t))

    plt.imshow(bw_image, cmap="gray")
    plt.axis("off")
    plt.show()

    logger.info("Advent of Code 2024 | Day 14")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
