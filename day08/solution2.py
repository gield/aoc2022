def viewing_distance(tree_house: int, trees: list[int]) -> int:
    for d, t in enumerate(trees):
        if t >= tree_house:
            break
    return d + 1


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

grid = {}
edge_length = len(lines)
for row, line in enumerate(lines):
    for col, tree in enumerate(map(int, line)):
        grid[(row, col)] = tree

scores = []
for row in range(1, edge_length - 1):
    for col in range(1, edge_length - 1):
        tree_house = grid[(row, col)]
        scores.append(1)
        trees_top = [grid[(r, col)] for r in range(row - 1, -1, -1)]
        scores[-1] *= viewing_distance(tree_house, trees_top)
        trees_bottom = [grid[(r, col)] for r in range(row + 1, edge_length)]
        scores[-1] *= viewing_distance(tree_house, trees_bottom)
        trees_left = [grid[(row, c)] for c in range(col - 1, -1, -1)]
        scores[-1] *= viewing_distance(tree_house, trees_left)
        trees_right = [grid[(row, c)] for c in range(col + 1, edge_length)]
        scores[-1] *= viewing_distance(tree_house, trees_right)
print(max(scores))
