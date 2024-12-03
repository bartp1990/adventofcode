"""Solution for https://adventofcode.com/2015/1."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        dims = [list(map(int, line.strip().split("x"))) for line in f.readlines()]

    total = 0
    for dim in dims:
        length = dim[0]
        width = dim[1]
        height = dim[2]
        total += (
            2 * length * width
            + 2 * width * height
            + 2 * height * length
            + sorted(dim)[0] * sorted(dim)[1]
        )

    print(total)

    total = 0
    for dim in dims:
        dim.sort()
        total += 2 * dim[0] + 2 * dim[1] + (dim[0] * dim[1] * dim[2])

    print(total)
