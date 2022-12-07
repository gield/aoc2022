with open("input.txt", "r") as f:
    lines = [l.strip().split(",") for l in f.readlines()]

num_overlap = 0
for elf1, elf2 in lines:
    elf1_l, elf1_r = [int(i) for i in elf1.split("-")]
    elf2_l, elf2_r = [int(i) for i in elf2.split("-")]
    if set(range(elf1_l, elf1_r + 1)) & set(range(elf2_l, elf2_r + 1)):
        num_overlap += 1
print(num_overlap)
