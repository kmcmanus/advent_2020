from itertools import combinations, chain

def invalid_number(data, header_length):
    for i, element in enumerate(data[header_length:], header_length):
        preamble = data[i-header_length:i]
        pre_pairs = combinations(preamble, 2)
        pre_sums = map(sum, pre_pairs)
        if element not in pre_sums:
            return element

def variable_combinations(data):
    for length in range(2, len(data)):
        for start in range(len(data) - length + 1):
            yield data[start:start+length]

def keys(data, value):
    for datas in variable_combinations(data):
        if sum(datas) == value:
            return (
                min(datas),
                max(datas)
            )


with open('input', 'r') as f:
    all_data = f.read()
    data = [
        int(line)
        for line in all_data.split("\n")
        if line
    ]


print("one")
value = invalid_number(data, 25)
print(value)

print("two")
print(sum(keys(data, value)))

