with open("input.txt", "r") as f:
    lines = [l.strip().split(",") for l in f.readlines()]

num_fully_contained = 0
for elf1, elf2 in lines:
    elf1_l, elf1_r = [int(i) for i in elf1.split("-")]
    elf2_l, elf2_r = [int(i) for i in elf2.split("-")]
    if (elf1_l <= elf2_l and elf1_r >= elf2_r) or (elf2_l <= elf1_l and elf2_r >= elf1_r):
        num_fully_contained += 1
print(num_fully_contained)
