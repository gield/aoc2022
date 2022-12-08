with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

grid = {}
edge_length = len(lines)
for row, line in enumerate(lines):
    for col, tree in enumerate(map(int, line)):
        grid[(row, col)] = tree

num_visible = edge_length * 4 - 4
for row in range(1, edge_length - 1):
    for col in range(1, edge_length - 1):
        tree = grid[(row, col)]
        if (
            all(grid[(r, col)] < tree for r in range(row))
            or all(grid[(r, col)] < tree for r in range(row + 1, edge_length))
            or all(grid[(row, c)] < tree for c in range(col))
            or all(grid[(row, c)] < tree for c in range(col + 1, edge_length))
        ):
            num_visible += 1
print(num_visible)
