"""Solution for https://adventofcode.com/2024/day/12."""

import logging
import numpy as np

from dataclasses import dataclass, field
from enum import Enum, auto

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@dataclass
class Region:
    letter: str
    rows: dict = field(default_factory=dict)
    area: int = 0
    perimeter: int = 0
    min_x: int = 999999999999
    max_x: int = 0
    min_y: int = 999999999999
    max_y: int = 0
    outside_edges_touched: int = 0
    edges: int = 0

    def get_subgrid_of_region(self, grid):
        return grid[self.min_y : self.max_y + 1, self.min_x : self.max_x + 1]

    def find_edges(self):
        n_edges = 4
        for i in range(0, len(self.rows) - 1):
            if not i + 1 in self.rows:
                break

            min_x_current = min(self.rows[i])
            max_x_current = max(self.rows[i])
            min_x_next = min(self.rows[i + 1])
            max_x_next = max(self.rows[i + 1])

            len_row_next = max_x_next - min_x_next
            len_row_current = max_x_current - min_x_current

            if (
                len_row_next == len_row_current
                and min_x_next == min_x_current
                and max_x_next == max_x_current
            ):
                continue
            elif (
                min_x_next != min_x_current
                and max_x_next != max_x_current
                and len_row_next != len_row_current
            ):
                n_edges += 4
            elif (
                min_x_next == min_x_current or max_x_next == max_x_current
            ) and len_row_next != len_row_current:
                n_edges += 2

        subgrid = self.get_subgrid_of_region(grid)
        print_grid(subgrid)

        return n_edges


def find_regions_in_grid(grid):
    shape = grid.shape
    visited = set()
    regions = []
    for y in range(0, shape[0]):
        for x in range(0, shape[1]):
            coord = (x, y)
            if coord not in visited:
                letter = grid[*coord]
                region = find_region(coord, letter, visited)
                regions.append(region)
    return regions


def print_grid(grid: np.ndarray):
    for row in grid:
        print("".join(row))
    print("\n")


def find_region(coord, char, visited):
    region = Region(letter=char)

    stack = [coord]

    while stack:
        current_coord = stack.pop()
        if current_coord in visited:
            continue
        visited.add(current_coord)

        region.area += 1
        if current_coord[0] not in region.rows:
            region.rows[current_coord[0]] = []
        region.rows[current_coord[0]].append(current_coord[1])

        if current_coord[0] in (0, shape[0]):
            region.outside_edges_touched += 1
        if current_coord[1] in (0, shape[1]):
            region.outside_edges_touched += 1

        neighbours = [
            (current_coord[0] - 1, current_coord[1]),
            (current_coord[0] + 1, current_coord[1]),
            (current_coord[0], current_coord[1] - 1),
            (current_coord[0], current_coord[1] + 1),
        ]

        for n_coord in neighbours:
            if 0 <= n_coord[0] < shape[0] and 0 <= n_coord[1] < shape[1]:
                if grid[n_coord[0], n_coord[1]] == char and n_coord not in visited:
                    stack.append(n_coord)
                elif grid[n_coord[0], n_coord[1]] != char:
                    region.perimeter += 1
            else:
                region.perimeter += 1

            region.min_y = min(region.rows.keys())
            region.max_y = max(region.rows.keys())
            region.min_x = min(min(lst) for lst in region.rows.values())
            region.max_x = max(max(lst) for lst in region.rows.values())

    region.edges = region.find_edges()

    return region


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    tmp_grid = []
    for i_row, line in enumerate(lines):
        row = []
        for i_col, char in enumerate(list(line.strip())):
            row.append(char)

        tmp_grid.append(row)

    grid = np.array(tmp_grid)
    shape = grid.shape

    part_1 = 0
    part_2 = 0
    regions = find_regions_in_grid(grid)
    for region in regions:
        logger.info(region)
        part_1 += region.area * region.perimeter
        part_2 += region.area * region.edges

    logger.info("Advent of Code 2024 | Day 12")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
