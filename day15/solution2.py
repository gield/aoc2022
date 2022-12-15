from typing import Iterator, Tuple


def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)


def calculate_border(sy: int, sx: int, d: int) -> Iterator[Tuple[int, int]]:
    for xrange in [range(sx - d, sx + 1), range(sx + d, sx, -1)]:
        dy = 0
        for x in xrange:
            y1 = sy + dy
            y2 = sy - dy
            dy += 1
            if x not in max_range or y1 not in max_range or y2 not in max_range:
                continue
            yield y1, x
            yield y2, x


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

max_range = range(4_000_001)
sensors = []
possible_locations = set()
for i, line in enumerate(lines):
    (sx, sy), (bx, by) = [tuple(map(int, xy.split("x=")[1].split(", y="))) for xy in line.split(":")]
    d = manhattan(sx, sy, bx, by)
    sensors.append((d, sy, sx))
    possible_locations |= set(calculate_border(sy, sx, d + 1))

sensors = sorted(sensors, reverse=True)
for i, (y, x) in enumerate(possible_locations):
    for d, sy, sx in sensors:
        if manhattan(x, y, sx, sy) <= d:
            break
    else:
        print(4_000_000 * x + y)
        break
