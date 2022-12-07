with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

sum_priorities = 0
for i in range(0, len(lines), 3):
    r1, r2, r3 = lines[i:i + 3]
    shared = next(iter(set(r1) & set(r2) & set(r3)))
    priority = ord(shared) - 96
    if priority <= 0:
        priority += 58
    sum_priorities += priority
print(sum_priorities)
