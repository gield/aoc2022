def compare(p1, p2) -> int:
    for left, right in zip(p1, p2):
        if type(left) is list or type(right) is list:
            if type(left) is not list:
                left = [left]
            elif type(right) is not list:
                right = [right]
            comparison = compare(left, right)
            if comparison != 0:
                return comparison
        elif left != right:
            return left - right
    return len(p1) - len(p2)


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

sum_indices = 0
pairs = "\n".join(lines).split("\n\n")
for i, pair in enumerate(pairs):
    p1, p2 = map(eval, pair.split("\n"))
    if compare(p1, p2) < 0:
        sum_indices += i + 1
print(sum_indices)
