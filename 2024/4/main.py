"""Solution for https://adventofcode.com/2024/day/4."""

import logging

import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

WORD_TO_FIND = "XMAS"


def rotate_90_deg(matrix):
    """Rotate a matrix 90 degrees."""
    transposed = [list(row) for row in zip(*matrix)]
    for row in transposed:
        row.reverse()

    return transposed


def get_diagonals(matrix):
    """Get all diagonals of a matrix."""
    matrix = np.array(matrix)
    flipped_matrix = np.fliplr(matrix)
    rows, cols = matrix.shape

    main_diagonals = []
    for offset in range(-rows + 1, cols):
        main_diagonals.append(matrix.diagonal(offset=offset).tolist())

    anti_diagonals = []
    for offset in range(-rows + 1, cols):
        anti_diagonals.append(flipped_matrix.diagonal(offset=offset).tolist())

    return main_diagonals, anti_diagonals


def count_word_in_lines(lines, word):
    """Count occurrences of the word in the list of lines."""
    return sum(line.count(word) for line in lines)


def extract_3x3_grids(grid, center_marker="A"):
    """
    Given a center letter, subtract the 3x3 subgrid around the center.

    In addition, apply a mask to the characters that do not matter for matching the search pattern.
    """
    rows = len(grid)
    cols = len(grid[0])
    subgrids = []

    for i in range(1, rows - 1):  # Start at 1 to avoid boundary issues
        for j in range(1, cols - 1):  # Start at 1 to avoid boundary issues
            if grid[i][j] == center_marker:
                # Extract the 3x3 grid centered on (i, j)
                subgrid = [row[j - 1 : j + 2] for row in grid[i - 1 : i + 2]]
                subgrids.append(subgrid)

    # Prepare subgrid for pattern matching by sanitizing
    for subgrid in subgrids:
        subgrid[0][1] = "."
        subgrid[1][0] = "."
        subgrid[1][2] = "."
        subgrid[2][1] = "."

    return subgrids


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    diag1, diag2 = get_diagonals(grid)
    diag3, diag4 = [diag[::-1] for diag in diag1], [diag[::-1] for diag in diag2]

    rotated_90_grids = [grid]
    for _ in range(3):
        rotated_90_grids.append(rotate_90_deg(rotated_90_grids[-1]))

    all_grids = rotated_90_grids[:]
    all_grids.extend([diag1, diag2, diag3, diag4])

    part_1 = sum(
        [count_word_in_lines(["".join(row) for row in grid], WORD_TO_FIND) for grid in all_grids]
    )

    SEARCH_TARGET = [
        ["M", ".", "M"],
        [".", "A", "."],
        ["S", ".", "S"],
    ]

    search_targets = [SEARCH_TARGET]
    for _ in range(3):
        search_targets.append(rotate_90_deg(search_targets[-1]))

    subgrids = extract_3x3_grids(grid)
    part_2 = sum(1 for subgrid in subgrids if subgrid in search_targets)

    logger.info("Advent of Code 2024 | Day 4")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
