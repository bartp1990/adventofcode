"""Solution for https://adventofcode.com/2024/day/9."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_checksum(blocks: list) -> int:
    checksum = 0
    for index, number in enumerate(blocks):
        if str(number) != ".":
            checksum += int(number) * index

    return checksum


def get_blocks(line: list):
    blocks = []
    file_offset = 0
    file_table = dict()
    counter = 0
    for i in range(0, len(line), 2):
        file_content = [counter] * line[i]
        blocks.extend(file_content)
        file_table[counter] = (counter, file_offset, len(file_content))
        file_offset += len(file_content)
        if i + 1 < len(line):
            free_space = ["."] * line[i + 1]
            blocks.extend(free_space)
            file_offset += len(free_space)
        counter += 1

    return blocks, file_table


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


def find_consecutive_free_space(blocks):
    indices = []
    start = None

    for i in range(len(blocks)):
        if blocks[i] == ".":
            if start is None:
                start = i
        else:
            if start is not None:
                indices.append((start, i))
                start = None

    if start is not None:
        indices.append((start, len(blocks)))

    return indices


def format_part_2(blocks: list, file_table: dict) -> list:
    blocks = blocks.copy()
    files = list(value for value in file_table.values())

    for num, offset, size in sorted(files, key=lambda x: x[0], reverse=True):
        for space in find_consecutive_free_space(blocks):
            diff = space[1] - space[0]
            if diff >= size:
                if offset < space[0]:
                    break

                blocks[space[0] : space[0] + size] = blocks[offset : offset + size]
                blocks[offset : offset + size] = ["."] * size

    return blocks


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read()

    disk = list(map(int, list(line.strip())))
    blocks, file_table = get_blocks(disk)

    part_1 = get_checksum(format_part_1(blocks))
    part_2 = get_checksum(format_part_2(blocks, file_table))

    logger.info("Advent of Code 2024 | Day 9")
    logger.info(f"Answer part 1: {part_1}")
    logger.info(f"Answer part 2: {part_2}")
