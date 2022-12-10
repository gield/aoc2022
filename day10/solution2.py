with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

instructions = []
for l in lines:
    instructions.append(0)
    if l.startswith("addx"):
        instructions.append(int(l.split()[1]))

x = 1
crt = [["."] * 40 for _ in range(6)]
for cycle in range(len(instructions)):
    r, c = divmod(cycle, 40)
    if abs(x - c) <= 1:
        crt[r][c] = "#"
    x += instructions[cycle]
for row in crt:
    print("".join(row))
