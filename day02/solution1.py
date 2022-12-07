with open("input.txt", "r") as f:
    lines = [l.strip().split() for l in f.readlines()]

total_score = 0
for other, you in lines:
    you = {"X": "A", "Y": "B", "Z": "C"}[you]
    if other == you:
        total_score += 3
    elif (other, you) in {("A", "B"), ("B", "C"), ("C", "A")}:
        total_score += 6
    total_score += {"A": 1, "B": 2, "C": 3}[you]
print(total_score)
