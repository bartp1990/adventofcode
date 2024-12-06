"""Solution for https://adventofcode.com/2024/day/6."""

import logging
from enum import Enum

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "V"
    LEFT = "<"


NEXT_DIR_MAP = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}


char_to_direction = {member.value: member for member in Direction}


class Grid:
    def __init__(self, lines):
        self.grid = []
        self.positions_visited = set()
        self.pos = None
        self.direction: Direction
        self.move_count = 0
        self.done = False

        tmp_grid = []
        for i_row, line in enumerate(lines):
            row = []
            for i_col, char in enumerate(list(line.strip())):
                row.append(char)
                if char in [direction.value for direction in Direction]:
                    self.pos = (i_row, i_col)
                    self.starting_pos = self.pos
                    self.direction = char_to_direction[char]

            tmp_grid.append(row)
            self.grid = np.array(tmp_grid)

    def move(self):
        self.positions_visited.add(self.pos)
        self.move_count += 1
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
        if not (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols):
            self.done = True
            return

        if new_pos and self.grid[*new_pos] != "#":
            self.pos = new_pos
            return

        self.direction = NEXT_DIR_MAP[self.direction]

    def __str__(self):
        return str(self.grid) + "\n"


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    grid = Grid(lines)

    while not grid.done:
        grid.move()

    print(f"Done! Visited: {len(grid.positions_visited)}")
    loop_positions = set()
    for i, position in enumerate(grid.positions_visited):
        print(i, len(grid.positions_visited), len(loop_positions))
        g = Grid(lines)
        g.grid[*position] = "#"

        while g.move_count < 100_000:
            g.move()

        if not g.done:
            loop_positions.add(position)

    print("Loops:", len(loop_positions))
