with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

sum_priorities = 0
for rucksack in lines:
    half_len = int(len(rucksack) / 2)
    c1, c2 = rucksack[:half_len], rucksack[half_len:]
    shared = next(iter(set(c1) & set(c2)))
    priority = ord(shared) - 96
    if priority <= 0:
        priority += 58
    sum_priorities += priority
print(sum_priorities)
