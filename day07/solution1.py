from typing import Optional, Union


class Directory(object):
    def __init__(self, name: str, parent: Optional['Directory']) -> None:
        self.name = name
        self.parent = parent or self  # hack for mypy
        self.children: set[Union[Directory, File]] = set()

    @property
    def size(self) -> int:
        return sum(c.size for c in self.children)


class File(object):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

root = Directory("", None)
current_dir = root
for line in lines[1:]:
    if line == "$ ls" or line.startswith("dir"):
        continue
    elif line.startswith("$ cd"):
        dir_name = line[5:]
        if dir_name == "..":
            current_dir = current_dir.parent
        else:
            new_dir = Directory(dir_name, current_dir)
            current_dir.children.add(new_dir)
            current_dir = new_dir
    else:
        size, filename = line.split()
        current_dir.children.add(File(filename, int(size)))

total_size = 0
visited: set[Directory] = set()
to_visit = {root}
while to_visit:
    current_dir = to_visit.pop()
    to_visit |= {c for c in current_dir.children if isinstance(c, Directory)}
    if current_dir.size <= 100_000:
        total_size += current_dir.size
print(total_size)
