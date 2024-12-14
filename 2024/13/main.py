import logging
import re
import sympy as sp

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

        print(f"Buttons: {buttons}")
        print(f"Prize: {prize}")

        a, b = sp.symbols('a b', integer=True)

        eq1 = sp.Eq(a * buttons["A"][0] + b * buttons["B"][0], prize[0] + 10000000000000)
        eq2 = sp.Eq(a * buttons["A"][1] + b * buttons["B"][1], prize[1] + 10000000000000)

        solution = sp.solve((eq1, eq2), (a, b))

        print(f"Solution: {solution}")

        if solution:
            a_val = solution[a]
            b_val = solution[b]

            cost = cost_per_button["A"] * a_val + cost_per_button["B"] * b_val
            print(f"Cost for this case: {cost}")
            lowest_cost += cost
            # Calculate the cost

    print(f"Total lowest cost: {lowest_cost}")

    part2 = lowest_cost

    logger.info("Advent of Code 2024 | Day 1")
    # logger.info(f"Answer part 1: {part1}")
    logger.info(f"Answer part 2: {part2}")
