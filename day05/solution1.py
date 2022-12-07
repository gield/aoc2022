from collections import defaultdict
import re
from typing import DefaultDict


with open("input.txt", "r") as f:
    lines = [l.rstrip() for l in f.readlines()]

stacks: DefaultDict[int, list[str]] = defaultdict(list)
for l in lines[:lines.index("")]:
    for i, j in enumerate(range(1, len(l), 4)):
        crate = l[j:j + 1]
        if crate == " " or crate.isnumeric():
            continue
        stacks[i + 1].insert(0, crate)

for l in lines[lines.index("") + 1:]:
    num, fr, to = map(int, re.findall(r"move (\d+) from (\d+) to (\d+)", l)[0])
    for _ in range(num):
        stacks[to].append(stacks[fr].pop())

print("".join(stacks[i][-1] for i in sorted(stacks.keys())))
