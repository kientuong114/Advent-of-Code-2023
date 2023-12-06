import sys

import math

def part1(inp: list[str]):
    times = map(int, inp[0].lstrip("Time:").split())
    distances = map(int, inp[1].lstrip("Distance:").split())

    l = []
    for t, d in zip(times, distances):
        discr = math.sqrt(t**2 - 4*d)

        t_high = (t + discr)/2
        t_low = (t - discr)/2

        t_high = int(t_high) - 1 if t_high.is_integer() else math.floor(t_high)
        t_low = int(t_low) + 1 if t_low.is_integer() else math.ceil(t_low)

        l.append(t_high - t_low + 1)

    return math.prod(l)


def part2(inp: list[str]):
    times = [int(''.join(inp[0].lstrip("Time:").split()))]
    distances = [int(''.join(inp[1].lstrip("Distance:").split()))]

    l = []
    for t, d in zip(times, distances):
        discr = math.sqrt(t**2 - 4*d)

        t_high = (t + discr)/2
        t_high = int(t_high) - 1 if t_high.is_integer() else math.floor(t_high)

        t_low = (t - discr)/2
        t_low = int(t_low) + 1 if t_low.is_integer() else math.ceil(t_low)

        l.append(t_high - t_low + 1)

    return math.prod(l)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = "6.alt"
    else:
        file = "6.in"

    with open(file) as f:
        inp = [line.strip() for line in f.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
