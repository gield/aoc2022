with open("input.txt", "r") as f:
    line = f.read().strip()

d = 4
for i in range(len(line) - d):
    if len(set(line[i:i + d])) == d:
        print(i + d)
        break
