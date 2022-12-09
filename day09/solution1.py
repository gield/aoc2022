def sign(x: int) -> int:
    if x < 0:
        return -1
    else:
        return 1


with open("input.txt", "r") as f:
    lines = [l.strip().split() for l in f.readlines()]

hx = hy = tx = ty = 0
visited = {(hx, hy)}
for motion, num_steps in lines:
    for _ in range(int(num_steps)):
        dx, dy = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}[motion]
        hx += dx
        hy += dy
        if abs(hx - tx) > 1:
            tx += sign(hx - tx)
            if abs(hy - ty) >= 1:
                ty += hy - ty
        elif abs(hy - ty) > 1:
            ty += sign(hy - ty)
            if abs(hx - tx) >= 1:
                tx += hx - tx
        visited.add((tx, ty))
print(len(visited))
