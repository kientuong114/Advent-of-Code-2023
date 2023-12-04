import sys
from dataclasses import dataclass

@dataclass
class Card:
    n_copies: int
    points: int

def parse_line(line: str) -> Card:
    _, cards = line.split(': ')
    win_list, have_list = cards.split(' | ')
    win = set(win_list.split())
    have = set(have_list.split())
    return Card(1, len(have.intersection(win)))

def part1(inp: list[str]):
    s = 0
    for line in inp:
        card = parse_line(line)
        s += 2**(card.points - 1) if card.points > 0 else 0
    return s

def part2(inp: list[str]):
    scratchcards = [parse_line(line) for line in inp]

    for idx, card in enumerate(scratchcards):
        if card.points == 0:
            continue

        for i in range(idx + 1, min(len(scratchcards), idx + card.points + 1)):
            scratchcards[i].n_copies += card.n_copies

    return sum(card.n_copies for card in scratchcards)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = "4.alt"
    else:
        file = "4.in"

    with open(file) as f:
        inp = [line.strip() for line in f.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
