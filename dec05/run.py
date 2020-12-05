from functools import reduce
from itertools import combinations
from collections import defaultdict
import re

def binary_count(line, low_char, high_char):
    return int(line.replace(low_char, "0").replace(high_char, "1"), 2)

assert binary_count("BFFFBBF", "F", "B") == 70
assert binary_count("FFFBBBF", "F", "B") == 14
assert binary_count("BBFFBBF", "F", "B") == 102

assert binary_count("RRR", "L", "R") == 7
assert binary_count("RLL", "L", "R") == 4

class BoardingPass(object):
    def __init__(self, line):
        self.line = line

    def get_row(self):
        return binary_count(self.line[0:7], "F", "B")

    def get_column(self):
        return binary_count(self.line[7:], "L", "R")

    def get_id(bp):
        return (bp.get_row() * 8) + bp.get_column()



boarding_passes = []
with open('input', 'r') as f:
    all_data = f.readlines()
    boarding_passes = [
        BoardingPass(line.strip())
        for line in all_data
    ]

ids = [
    bp.get_id()
    for bp in boarding_passes
]
max_id = max(ids)
print("one")
print(max_id)

gaps = [
  i
  for i in xrange(max_id)
  if i not in ids
]


print("two")
print(gaps)
