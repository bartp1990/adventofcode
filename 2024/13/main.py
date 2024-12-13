"""Solution for https://adventofcode.com/2024/day/1."""

import logging
import re
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()

    cost_per_button = {
        "A": 3,
        "B": 1,
    }

    cases = content.split("\n\n")

    button_pattern = r"X\+(\d+), Y\+(\d+)"
    prize_pattern = r"X=(\d+), Y=(\d+)"
    buttons = dict()
    lowest_cost = 0
    for case in cases:
        tmp = [(int(x), int(y)) for x, y in re.findall(button_pattern, case)]
        buttons["A"] = tmp[0]
        buttons["B"] = tmp[1]
        prize_match = re.search(prize_pattern, case)
        prize = int(prize_match.group(1)), int(prize_match.group(2))

        max_presses = dict()
        for name, (x, y) in buttons.items():
            max_presses_x = prize[0] // x
            max_presses_y = prize[1] // y
            max_presses[name] = min(max_presses_x, max_presses_y)

        min_cost = math.inf
        for a in range(0, max_presses["A"] + 1):
            for b in range(0, max_presses["B"] + 1):
                X = buttons["A"][0] * a + buttons["B"][0] * b
                Y = buttons["A"][1] * a + buttons["B"][1] * b

                if not X == prize[0] or not Y == prize[1]:
                    continue

                cost = cost_per_button["A"] * a + cost_per_button["B"] * b
                if cost < min_cost:
                    min_cost = cost

        # print(min_cost)
        lowest_cost += min_cost if min_cost != math.inf else 0

    print(lowest_cost)

    part1 = None
    part2 = None

    logger.info("Advent of Code 2024 | Day 1")
    logger.info(f"Answer part 1: {part1}")
    logger.info(f"Answer part 2: {part2}")
