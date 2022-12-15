def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

y = 2_000_000
positions_with_beacon = set()
positions_without_beacon = set()
for line in lines:
    (sx, sy), (bx, by) = [tuple(map(int, xy.split("x=")[1].split(", y="))) for xy in line.split(":")]
    if sy == y:
        positions_with_beacon.add((sx, sy))
    if by == y:
        positions_with_beacon.add((bx, by))
    d = manhattan(sx, sy, bx, by)
    if y in range(sy - d, sy + d + 1):
        for x in range(sx - d, sx + d + 1):
            if manhattan(sx, sy, x, y) <= d:
                positions_without_beacon.add((x, y))
print(len(positions_without_beacon - positions_with_beacon))
