def sign(x: int) -> int:
    if x < 0:
        return -1
    else:
        return 1


with open("input.txt", "r") as f:
    lines = [l.strip().split() for l in f.readlines()]

rope = [(0, 0)] * 10
visited = {(0, 0)}
for motion, num_steps in lines:
    for _ in range(int(num_steps)):
        dx, dy = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}[motion]
        rope[0] = (rope[0][0] + dx, rope[0][1] + dy)
        for i in range(9):
            (hx, hy), (tx, ty) = rope[i], rope[i + 1]
            if abs(hx - tx) > 1:
                tx += sign(hx - tx)
                if abs(hy - ty) >= 1:
                    ty += sign(hy - ty)
            elif abs(hy - ty) > 1:
                ty += sign(hy - ty)
                if abs(hx - tx) >= 1:
                    tx += sign(hx - tx)
            rope[i + 1] = (tx, ty)
        visited.add(rope[-1])
print(len(visited))
