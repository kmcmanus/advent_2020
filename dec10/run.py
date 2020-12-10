import functools

def memo(func):
  res = {}
  def wrapped(*args):
    if not args in res:
      args[res] = func(res)
    return args[res]
  return wrapped

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

def get_args(data):
  bits = [int(d) for d in data.split(",")]
  return (bits[0], bits[1:])

def from_args(first, rest):
  return ",".join(str(i) for i in [first] + rest)

@functools.lru_cache
def valid_combinations(data):
    first, rest = get_args(data)
    if len(rest) == 1:
        if rest[0] - first <= 3:
            return 1
        return 0
    return sum([
        valid_combinations(from_args(item, rest[i:]))
        for i, item in enumerate(rest[0:3], 1)
        if item - first <= 3
    ])

print("two")
print(valid_combinations(from_args(0, data + [data[-1]+3])))
