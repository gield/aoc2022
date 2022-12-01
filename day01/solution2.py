with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

elves = [sum(map(int, elf.split("\n"))) for elf in "\n".join(lines).split("\n\n")]
print(sum(sorted(elves)[-3:]))
