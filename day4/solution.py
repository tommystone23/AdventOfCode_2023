import re

def part1(data: list[str]):
    total = 0
    for line in data:
        winning_nbs, our_nbs = parse_line(line)
        tally = 0
        for nb in our_nbs:
            if nb in winning_nbs:
                tally += tally if tally > 0 else 1
        total += tally
    print(total)
    

def part2(data : list[str]):
    cards = [1] * len(data)
    total = 0
    for i, line in enumerate(data):
        winning_nbs, our_nbs = parse_line(line)
        wins = 0
        for nb in our_nbs:
            if nb in winning_nbs:
                wins += 1
        for j in range(cards[i]):
            for k in range(i+1, (i+1) + wins):
                cards[k] += 1
        total += cards[i]
    print(total)

def parse_line(line : str):
    pipe_split = re.split(r"\|", line)
    winning_nbs = re.split(r"\s+", pipe_split[0].strip())
    winning_nbs = winning_nbs[2:]
    our_nbs = re.split(r"\s+", pipe_split[1].strip())
    return winning_nbs, our_nbs

with open('data_set.txt') as f:
    data = f.readlines()

part1(data)
part2(data)