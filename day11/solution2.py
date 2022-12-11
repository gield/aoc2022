from functools import reduce
from typing import Any


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

monkeys: list[dict[str, Any]] = []
for i in range(0, len(lines), 7):
    monkeys.append({
        "items": [int(item) for item in lines[i + 1][16:].split(", ")],
        "operation": lines[i + 2][17:],
        "test": int(lines[i + 3][19:]),
        "monkey_true": int(lines[i + 4][25:]),
        "monkey_false": int(lines[i + 5][26:]),
    })

lcm = reduce((lambda x, y: x * y), [m["test"] for m in monkeys])
inspections = [0] * len(monkeys)
for _ in range(10_000):
    for m, monkey in enumerate(monkeys):
        for old in monkey["items"]:
            inspections[m] += 1
            item = eval(monkey["operation"]) % lcm
            k = "monkey_false" if item % monkey["test"] else "monkey_true"
            monkeys[monkey[k]]["items"].append(item)
        monkey["items"] = []
m1, m2 = sorted(inspections)[-2:]
print(m1 * m2)
