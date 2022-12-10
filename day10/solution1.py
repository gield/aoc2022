with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

instructions = []
for l in lines:
    instructions.append(0)
    if l.startswith("addx"):
        instructions.append(int(l.split()[1]))

x = 1
sum_signal_strength = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    x += sum(instructions[max(cycle - 40 - 1, 0):cycle - 1])
    sum_signal_strength += x * cycle
print(sum_signal_strength)
