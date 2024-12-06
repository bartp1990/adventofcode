"""Solution for https://adventofcode.com/2024/day/6."""

import logging
from enum import Enum
from time import sleep
import os

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "V"
    LEFT = "<"


char_to_direction = {member.value: member for member in Direction}


def get_next_direction(dir: Direction) -> Direction:
    next_dir_map = {
        Direction.UP: Direction.RIGHT,
        Direction.RIGHT: Direction.DOWN,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.UP,
    }

    return next_dir_map[dir]


class Grid:
    def __init__(self, f):
        self.grid = []
        self.pos = None
        self.direction: Direction
        self.total_visited = 1
        self.possible_obstacles = []

        tmp_grid = []
        for i_row, line in enumerate(f.readlines()):
            row = []
            for i_col, char in enumerate(list(line.strip())):
                row.append(char)
                if char in [direction.value for direction in Direction]:
                    self.pos = (i_row, i_col)
                    self.direction = char_to_direction[char]

            tmp_grid.append(row)
            self.grid = np.array(tmp_grid)

    def check_loop_if_turn(self, new_pos):
        rows, cols = self.grid.shape
        cells = []
        direction = get_next_direction(self.direction)

        if direction == Direction.UP:
            # Collect cells upwards, till we go out of bounds
            for r in range(self.pos[0] - 1, -1, -1):  # Move from start_row upwards (r-- till 0)
                cells.append((r, self.pos[1]))
        elif direction == Direction.DOWN:
            # Collect cells downwards, till we go out of bounds
            for r in range(self.pos[0] - 1, rows):  # Move from start_row downwards (r++ till rows)
                cells.append((r, self.pos[1]))
        elif direction == Direction.LEFT:
            # Collect cells leftwards, till we go out of bounds
            for c in range(self.pos[1] - 1, -1, -1):  # Move from start_col leftwards (c-- till 0)
                cells.append((self.pos[0], c))
        elif direction == Direction.RIGHT:
            # Collect cells rightwards, till we go out of bounds
            for c in range(self.pos[1] - 1, cols):  # Move from start_col rightwards (c++ till cols)
                cells.append((self.pos[0], c))

        for i, cell in enumerate(cells):
            print(self.grid[*cell])
            if self.grid[*cell] in [direction.value for direction in Direction] and self.grid[*cells[i+1]] == "#":
                self.possible_obstacles.append(new_pos)
            if self.grid[*cell] == "#":
                break

    def move(self):

        self.grid[*self.pos] = self.direction.value

        def get_new_pos(direction, pos):

            new_pos = None

            if direction is Direction.UP:
                new_pos = (pos[0] - 1, self.pos[1])
            elif direction is Direction.DOWN:
                new_pos = (pos[0] + 1, self.pos[1])
            elif direction is Direction.LEFT:
                new_pos = (pos[0], self.pos[1] - 1)
            elif direction is Direction.RIGHT:
                new_pos = (pos[0], self.pos[1] + 1)

            return new_pos

        new_pos = get_new_pos(self.direction, self.pos)

        rows, cols = self.grid.shape
        if not 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols:
            print(f"Done! Visited: {self.total_visited}, possible blockages: {len(set(self.possible_obstacles))}")
            exit(0)

        if new_pos and self.grid[*new_pos] != "#":
            if self.grid[*new_pos] not in [dir.value for dir in Direction]:
                self.total_visited += 1
            else:
                bla = 1

            self.check_loop_if_turn(new_pos=new_pos)

            self.pos = new_pos
        else:
            self.direction = get_next_direction(self.direction)

    def __str__(self):
        return str(self.grid) + "\n"


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = Grid(f)

    while True:
        grid.move()
