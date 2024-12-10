"""Solution for https://adventofcode.com/2024/day/10."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    distinct = 0

    with open("input.txt") as f:
        lines = f.readlines()

    trailheads = set()
    max_y = len(lines) - 1
    max_x = len(list(lines[0].strip())) - 1
    grid = []

    for i_row, line in enumerate(lines):
        row = []
        for i_col, char in enumerate(list(line.strip())):
            number = int(char)
            row.append(number)
            if number == 0:
                trailheads.add((i_row, i_col))
        grid.append(row)

    def valid_neighbours(coord, num):
        result = set()
        new_coords = (
            (coord[0] - 1, coord[1]),
            (coord[0] + 1, coord[1]),
            (coord[0], coord[1] - 1),
            (coord[0], coord[1] + 1),
        )

        for c in new_coords:
            if max_y < c[1] or c[1] < 0 or max_x < c[0] or c[0] < 0:
                continue
            if grid[c[0]][c[1]] == num + 1:
                result.add(c)

        return result

    def search_part1(coord, trail_peaks):
        cur_pos = grid[coord[0]][coord[1]]

        if cur_pos == 9:
            trail_peaks.append(coord)
            return

        for neighbour in valid_neighbours(coord, cur_pos):
            search_part1(neighbour, peaks)

    total_part_1 = 0
    total_part_2 = 0
    for head in trailheads:
        peaks = list()
        search_part1(head, peaks)
        total_part_1 += len(set(peaks))
        total_part_2 += len(peaks)

    part_1 = total_part_1
    part_2 = total_part_2

    logger.info("Advent of Code 2024 | Day 10")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
