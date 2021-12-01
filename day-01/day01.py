#!python

import sys

with open("input.day1") as f:
    # strip those pesky newlines and make a list of the data
    # we read strings but want values, so convert to int
    data = [int(line.strip()) for line in f.readlines()]
    count = 0
    for i, x in enumerate(data):
        if i > 0:
            if data[i] > data[i - 1]:
                count += 1
    print(count)
