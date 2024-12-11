"""Solution for https://adventofcode.com/2024/day/11."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    with open("input.txt") as f:
        stones = list(map(str, f.read().split()))

    def blink(stones) -> list:
        new_stones = []
        for stone in stones:
            stone_str = str(stone)
            l_stone_str = len(stone_str)
            if stone_str == "0":
                new_stones.append("1")
            elif l_stone_str % 2 == 0:
                half_index = l_stone_str // 2
                new_stones.append(int(stone_str[0:half_index]))
                new_stones.append(int(stone_str[half_index:]))
            else:
                new_stones.append(str(int(stone) * 2024))

        return new_stones

    # print("Initial arrangement:")
    # print(" ".join(list(map(str,stones))))
    # print("")

    for i in range(25):
        print(i)
        # blink_word = "blinks"
        # if i == 0:
        #     blink_word = "blink"25

        stones = blink(stones)
        # print(f"After {i+1} {blink_word}:")
        # print(" ".join(list(map(str,stones))))
        # print("")

    part_1 = len(stones)
    part_2 = None

    logger.info("Advent of Code 2024 | Day 11")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
