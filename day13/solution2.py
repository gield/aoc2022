from functools import cmp_to_key


def compare(p1, p2) -> int:
    for left, right in zip(p1, p2):
        if type(left) is list or type(right) is list:
            if type(left) is not list:
                left = [left]
            elif type(right) is not list:
                right = [right]
            comparison = compare(left, right)
            if comparison != 0:
                return comparison
        elif left != right:
            return left - right
    return len(p1) - len(p2)


with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

packets = [eval(p) for p in lines if p != ""] + [[[2]], [[6]]]
sorted_packets = sorted(packets, key=cmp_to_key(compare))
print((1 + sorted_packets.index([[2]])) * (1 + sorted_packets.index([[6]])))
