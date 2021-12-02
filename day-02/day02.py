#!python


from typing import List


class Location:
    def __init__(self, horizontal: int = 0, depth: int = 0):
        self.horizontal = horizontal
        self.depth = depth

    def __str__(self) -> str:
        return f"H:{self.horizontal} D:{self.depth}"


class Navigate:
    def __init__(self, location: Location, aim: int = 0):
        self.location: Location = location
        self.aim: int = aim

    def __str__(self) -> str:
        return f"H:{self.horizontal} D:{self.depth}"

    def forward(self, x: int):
        self.location.horizontal += x
        self.location.depth += self.aim * x

    def down(self, x: int):
        self.aim += x

    def up(self, x: int):
        self.aim -= x


def follow_route(data: List, start: Location) -> Location:
    current = start
    for item in data:
        # print(f"{item[0]} -> {item[1]}")
        if item[0] == "forward":
            current.horizontal += item[1]
        elif item[0] == "down":
            current.depth += item[1]
        elif item[0] == "up":
            current.depth -= item[1]

    return current


def follow_route_with_aim(data: List, start: Location) -> Location:
    current: Location = start
    submarine = Navigate(current)
    for item in data:
        if item[0] == "forward":
            submarine.forward(item[1])
        elif item[0] == "down":
            submarine.down(item[1])
        elif item[0] == "up":
            submarine.up(item[1])

    return submarine.location


with open("input.day2") as f:
    # strip those pesky newlines and make a list of the data
    # we're expecting a list of direction value pairs
    data = [(line.strip().split()) for line in f.readlines()]
    # we know the second item in each pair should be an int
    for item in data:
        item[1] = int(item[1])

    # part 1
    location = follow_route(data, Location())
    print(f"{location}: {location.horizontal * location.depth}")

    # part 2
    location = follow_route_with_aim(data, Location())
    print(f"{location}: {location.horizontal * location.depth}")
