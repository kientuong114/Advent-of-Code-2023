from collections import deque
import sys

def part1(inp: list[str]):
    seeds = map(int, inp[0].lstrip("seeds: ").split())

    mappings = []
    curr_map = []
    for line in inp[2:]:
        if 'map' in line:
            continue
        elif line == "":
            mappings.append(curr_map)
            curr_map = []
        else:
            dest_r, src_r, r_len = map(int, line.split())
            curr_map.append((dest_r, src_r, r_len))

    mappings.append(curr_map)

    min_loc = None

    for seed in seeds:
        curr_val = seed
        for mapping in mappings:
            for dest_r, src_r, r_len in mapping:
                if curr_val in range(src_r, src_r+r_len):
                    curr_val = dest_r + (curr_val - src_r)
                    break
        if min_loc is None or curr_val < min_loc:
            min_loc = curr_val
    return min_loc

def part2(inp: list[str]):
    seeds = list(map(int, inp[0].lstrip("seeds: ").split()))
    seed_ranges = [tuple(seeds[i:i+2]) for i in range(0, len(seeds), 2)]

    mappings = []
    curr_map = []
    for line in inp[2:]:
        if 'map' in line:
            continue
        elif line == "":
            mappings.append(curr_map)
            curr_map = []
        else:
            dest_r, src_r, r_len = map(int, line.split())
            curr_map.append((dest_r, src_r, r_len))

    mappings.append(curr_map)

    curr_ranges = deque(seed_ranges)

    for mapping in mappings:
        new_ranges = deque()

        while len(curr_ranges) > 0:
            myrange = curr_ranges.popleft()
            myrange_start, myrange_len = myrange

            for map_line in mapping:
                dest_r, src_r, r_len = map_line
                if src_r <= myrange_start < src_r + r_len:
                    # Case 1: the start of myrange is in the middle of one of the ranges
                    if myrange_start + myrange_len <= src_r + r_len:
                        # Case 1.a: the end of myrange is before the end of the other range
                        new_ranges.append((dest_r + (myrange_start - src_r), myrange_len))
                    else:
                        # Case 1.b: the end of myrange is after the end of the other range
                        new_ranges.append((dest_r + (myrange_start - src_r), src_r + r_len - myrange_start))
                        curr_ranges.append((src_r + r_len, myrange_len - (src_r + r_len - myrange_start) - 1))
                    break
                elif myrange_start <= src_r < myrange_start + myrange_len:
                    # Case 2: one of the ranges starts in the middle of myrange
                    curr_ranges.append((myrange_start, src_r - myrange_start))
                    curr_ranges.append((src_r, myrange_start + myrange_len - src_r))
                    break
            else:
                # Case 3: No range matches, pass through the current range
                new_ranges.append(myrange)

        curr_ranges = new_ranges

    return min(x[0] for x in curr_ranges)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = "5.alt"
    else:
        file = "5.in"

    with open(file) as f:
        inp = [line.strip() for line in f.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
