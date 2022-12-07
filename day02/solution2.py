with open("input.txt", "r") as f:
    lines = [l.strip().split() for l in f.readlines()]

total_score = 0
for other, result in lines:
    if result == "Y":
        you = other
    elif result == "Z":
        you = {"A": "B", "B": "C", "C": "A"}[other]
    else:
        you = {"B": "A", "C": "B", "A": "C"}[other]
    total_score += {"X": 0, "Y": 3, "Z": 6}[result]
    total_score += {"A": 1, "B": 2, "C": 3}[you]
print(total_score)
