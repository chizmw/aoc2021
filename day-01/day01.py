#!python

import sys

# read from the file
with open("input.day1") as f:
    # strip those pesky newlines and make a list of the data
    # we read strings but want values, so convert to int
    data = [int(line.strip()) for line in f.readlines()]
    count = 0
    prev = None
    for cur in data:
        if prev is not None:
            if cur > prev:
                count += 1
        prev = cur
    print(count)
