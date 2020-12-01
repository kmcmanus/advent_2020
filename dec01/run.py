from functools import reduce
from itertools import combinations

# A worse combinations
def chain(data, layers):
    for index, datum in enumerate(data):
        if layers == 1:
            yield [datum]
        else:
            for datas in chain(data[index+1:], layers - 1):
                yield datas + [datum]

def combine(data, layers):
    return [
      reduce(lambda x, y: x * y, bits, 1)
      for bits in combinations(data, layers)
      if sum(bits) == 2020
    ][0]

def one(data):
    for i, d in enumerate(data):
        for e in data[i+1:]:
            if d + e == 2020:
                return d * e

def two(data):
    for i, d in enumerate(data):
        for j, e in enumerate(data[i+1:]):
            for k, f in enumerate(data[j+1:]):
                if d + e +f == 2020:
                    return d * e * f


with open('input', 'r') as f:
    data = [int(d.strip()) for d in f.readlines()]
print(one(data))
print(combine(data, 2))
print(two(data))
print(combine(data, 3))
