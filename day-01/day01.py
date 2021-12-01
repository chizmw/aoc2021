#!python

import sys
from typing import List


def part1(data: List) -> int:
    count = 0
    for i, x in enumerate(data):
        if i > 0:
            if data[i] > data[i - 1]:
                count += 1
    return count


def part2(data: List) -> int:
    count = 0
    prev_sum = None
    for i, x in enumerate(data):
        if i > 2:
            prev_sum = sum(data[i - 4 : i - 1])
            curr_sum = sum(data[i - 3 : i])

            if curr_sum > prev_sum:
                count += 1

    return count


with open("input.day1") as f:
    # strip those pesky newlines and make a list of the data
    # we read strings but want values, so convert to int
    data = [int(line.strip()) for line in f.readlines()]
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
