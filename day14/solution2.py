from itertools import count


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

source = (0, 500)
grid = {source: "+"}
for line in lines:
    coords = [tuple(map(int, xy.split(","))) for xy in line.split(" -> ")]
    for (fx, fy), (tx, ty) in zip(coords[:-1], coords[1:]):
        for x in list(range(fx, tx + 1)) + list(range(tx, fx + 1)):
            grid[(fy, x)] = "#"
        for y in list(range(fy, ty + 1)) + list(range(ty, fy + 1)):
            grid[(y, fx)] = "#"

max_y = max(y for y, _ in grid.keys())
for t in count():
    if grid[source] == "O":
        print(t)
        break
    y, x = source
    while True:
        for dy, dx in [(1, 0), (1, -1), (1, 1)]:
            if (y + dy, x + dx) not in grid:
                y += dy
                x += dx
                break
        else:
            grid[(y, x)] = "O"
            break
        if y == max_y + 1:
            grid[(y, x)] = "O"
            break
