from functools import reduce
from itertools import combinations
from collections import defaultdict

# becasue we read rows and then columns, points are (y, x) and not (x, y)
row = lambda: defaultdict(int)
has_a_tree = defaultdict(row)
height = 0
width = 0
with open('input', 'r') as f:
    for y, row in enumerate(f.readlines()):
        for x, char in enumerate(row):
            if char == '#':
                has_a_tree[y][x] += 1
            width = x
        height = y

def add(point, speed):
    (py, px) = point
    (sy, sx) = speed
    return (py + sy, (px + sx) % width)

def tree_at(vec):
    return has_a_tree[vec[0]][vec[1]]

def hitting_trees(speed):
    position = (0, 0)
    trees = 0
    while position[0] <= height:
        position = add(position, speed)
        if tree_at(position):
            trees += 1
    return trees

print("One")
print(hitting_trees((1, 3)))

speeds = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
        ]
product = lambda items: reduce(lambda x, y: x * y, items, 1)

print("Two")
print(product([hitting_trees(s) for s in speeds]))
