"""Solution for https://adventofcode.com/2024/day/9."""

import logging
from dataclasses import dataclass
from typing import Self

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_checksum(blocks: list) -> int:
    checksum = 0
    for index, number in enumerate(blocks):
        if str(number) != ".":
            checksum += int(number) * index

    return checksum

def get_blocks(line: list) -> list:
    blocks = []
    counter = 0
    for i in range(0, len(line), 2):
        blocks.extend([counter] * line[i])
        if i + 1 < len(line):
            blocks.extend(["."] * line[i + 1])
        counter += 1

    return blocks

def format_part_1(blocks: list) -> list:
    blocks = blocks.copy()
    forward_index = 0
    backward_index = len(blocks) - 1

    while backward_index > forward_index:
        while blocks[forward_index] != ".":
            forward_index += 1

        while blocks[backward_index] == ".":
            backward_index -= 1

        if forward_index > backward_index:
            break

        blocks[forward_index] = blocks[backward_index]
        blocks[backward_index] = "."

    return blocks

def format_part_2(blocks: list) -> list:
    pass

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read()

    disk = list(map(int,list(line.strip())))
    blocks = get_blocks(disk)

    part_1 = get_checksum(format_part_1(blocks))
    # part_2 = get_checksum(format_part_2(chunks))

    logger.info("Advent of Code 2024 | Day 9")
    logger.info(f"Answer part 1: {part_1}")
    # logger.info(f"Answer part 2: {part_2}")
