import sys

def parse_line(line: str) -> tuple[int, list[dict[str, int]]]:
    game, record = line.split(": ")
    game = int(game.lstrip("Game "))

    records = [
        {
            color: int(count)
            for count, color in [
                # Split into the individual cube sets, then split each
                # into a count and a color
                s.split() for s in subset.split(', ')
            ]
        }
        # Split into subsets divided by a semicolon ;
        for subset in record.split('; ')
    ]

    return game, records

def part1(inp: list[str]):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    s = 0

    for line in inp:
        game, records = parse_line(line)
        impossible = False

        for record in records:
            for color, count in record.items():
                if count > limits[color]:
                    impossible = True
                    break

        if not impossible:
            s += game

    return s

def part2(inp: list[str]):
    s = 0

    for line in inp:
        _, records = parse_line(line)

        max_counts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for record in records:
            for color, count in record.items():
                max_counts[color] = max(max_counts[color], count)

        power = max_counts["red"] * max_counts["green"] * max_counts["blue"]
        s += power

    return s

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = "2.alt"
    else:
        file = "2.in"

    with open(file) as f:
        inp = [line.strip() for line in f.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
