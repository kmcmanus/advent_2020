from itertools import permutations
import math

def lengthed_iteration(data, length):
    return (
      data[start:start+length]
      for start in range(len(data) - length + 1)
    )

with open('input', 'r') as f:
    all_data = f.read()
    data = sorted([
        int(line)
        for line in all_data.split("\n")
        if line
    ])

def get_steps(data):
    steps = [None, 0, 0, 0]
    for (prev, curr) in lengthed_iteration([0] + data + [ data[-1] + 3], 2):
        steps[curr - prev] += 1
    return steps

print("one")
steps = get_steps(data)
print(steps[3] * steps[1])

def valid_combinations(start, rest, last):
    if not rest:
        if last - start <= 3:
            return 1
        return 0
    return sum([
        valid_combinations(item, rest[i:], last)
        for i, item in enumerate(rest[0:3], 1)
        if item - start <= 3
    ])

print("two")
print(valid_combinations(0, data, data[-1]+3))
