from queue import PriorityQueue
from typing import Tuple


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

grid = {}
for row, line in enumerate(lines):
    for col, elevation in enumerate(line):
        if elevation == "S":
            elevation = "a"
            start = (row, col)
        elif elevation == "E":
            elevation = "z"
            end = (row, col)
        grid[(row, col)] = elevation

graph: dict[Tuple[int, int], set[Tuple[int, int]]] = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        current = (y, x)
        graph[current] = set()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (y + dy, x + dx)
            if neighbor in grid and ord(grid[neighbor]) - ord(grid[current]) <= 1:
                graph[current].add(neighbor)

queue: PriorityQueue = PriorityQueue()
distances = {}
for square_a in [k for k, v in grid.items() if v == "a"]:
    queue.put((0, square_a))
    distances[square_a] = 0
visited = set()
while queue.qsize():
    d, square = queue.get()
    if square == end:
        print(d)
        break
    if square in visited:
        continue
    visited.add(square)
    d = distances[square]
    for neighbor in graph[square] - visited:
        if d + 1 < distances.get(neighbor, float('inf')):
            queue.put((d + 1, neighbor))
            distances[neighbor] = d + 1
