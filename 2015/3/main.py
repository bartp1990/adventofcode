"""Solution for https://adventofcode.com/2015/1."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.read()

    x, y = 0, 0

    presents = dict()
    presents[0] = {0: 1}

    for char in file:
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1
        else:
            raise ValueError(f"Unknown character {char}")

        if x not in presents:
            presents[x] = {}  # Create a new dictionary for x if it doesn't exist

        if y in presents[x]:
            presents[x][y] += 1
        else:
            presents[x][y] = 1

    total = 0
    for key, row in presents.items():
        total += sum(row.values())

    total = 0
    for key, row in presents.items():
        total += len(row.keys())

    print(total)
