from string import digits

def part1(inp: list[str]):
    subs_table = {}
    for d in digits:
        subs_table[d] = int(d)

    s = 0
    for line in inp:
        n = []
        for i in range(len(line)):
            for k, v in subs_table.items():
                if line[i:].startswith(k):
                    n.append(v)
        s += n[0] * 10 + n[-1]
        n = []
    return s

def part2_alt(inp: list[str]):
    subs_table = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for d in digits:
        subs_table[d] = int(d)

    s = 0
    for line in inp:
        n = []
        for i in range(len(line)):
            for k, v in subs_table.items():
                if line[i:].startswith(k):
                    n.append(v)
        s += n[0] * 10 + n[-1]
        n = []
    return s


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        file = "1.alt"
    else:
        file = "1.in"

    with open(file) as f:
        inp = [line.strip() for line in f.readlines()]


    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2_alt(inp)}")
