
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
print(two(data))
