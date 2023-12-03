import sys
from string import digits, printable


def find_number_in_line(line: str, start: int) -> tuple[int, int]:
    i = start
    ds = [line[i]]

    # Look for digits on left
    while True:
        i -= 1
        # Look for digits on left
        if i >= 0 and line[i] in digits:
            ds.insert(0, line[i])
        else:
            break

    # Look for digits on right
    i = start
    while True:
        i += 1
        if i < len(line) and line[i] in digits:
            ds.append(line[i])
        else:
            break

    num = int(''.join(ds))
    return num, i - 1

def part1(inp: list[str]):
    s = 0
    inserted = set()
    symbols = set(printable) - set(['.', '\n'] + list(digits))

    for idx, line in enumerate(inp):
        if all(ch not in line for ch in symbols):
            continue

        prev = inp[idx - 1] if idx > 0 else '.' * len(inp[0])
        follow = inp[idx + 1] if idx < len(inp) - 1 else '.' * len(inp[0])
        curr = inp[idx]

        for col, ch in enumerate(curr):
            if ch not in symbols:
                continue

            # Create a list consisting of places where we need to look for numbers
            # Each tuple contains the line index, the line itself, the list of points from where to look for numbers
            # Numbers may overlap. e.g.
            #
            # 123
            # .*.
            # ...
            # 
            # May get counted twice, but due to the duplicate check, we avoid summing
            starts = [
                (
                    row_idx,
                    line,
                    [col_idx for col_idx in (col+1, col, col-1) if line[col_idx] in digits]
                ) for row_idx, line in zip([idx-1, idx, idx+1], (prev, curr, follow))
            ]

            for row_idx, line, starts_row, in starts:
                for start in starts_row:
                    num, last_idx = find_number_in_line(line, start)
                    if (row_idx, last_idx) not in inserted:
                        s += num
                        inserted.add((row_idx, last_idx))

    return s

def part2(inp: list[str]):
    s = 0
    inserted = set()
    symbols = set('*')

    for idx, line in enumerate(inp):
        if all(ch not in line for ch in symbols):
            continue

        prev = inp[idx - 1] if idx > 0 else '.' * len(inp[0])
        follow = inp[idx + 1] if idx < len(inp) - 1 else '.' * len(inp[0])
        curr = inp[idx]

        for col, ch in enumerate(curr):
            if ch not in symbols:
                continue

            n_found = 0
            ratio = 1

            # Create a list consisting of places where we need to look for numbers
            # Each tuple contains the line index, the line itself, the list of points from where to look for numbers
            # Numbers may overlap. e.g.
            #
            # 123
            # .*.
            # ...
            # 
            # May get counted twice, but due to the duplicate check, we avoid summing
            starts = [
                (
                    row_idx,
                    line,
                    [col_idx for col_idx in (col+1, col, col-1) if line[col_idx] in digits]
                ) for row_idx, line in zip([idx-1, idx, idx+1], (prev, curr, follow))
            ]

            for row_idx, line, starts_row, in starts:
                for start in starts_row:
                    num, last_idx = find_number_in_line(line, start)
                    if (row_idx, last_idx) not in inserted:
                        n_found += 1
                        ratio *= num
                        inserted.add((row_idx, last_idx))

            if n_found == 2:
                s += ratio

    return s

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = "3.alt"
    else:
        file = "3.in"

    with open(file) as f:
        inp = [line.strip() for line in f.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
