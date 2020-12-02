
class Policy(object):
    def __init__(self, policy):
        bits = policy.split(' ')
        self.full_char_range = bits[0]
        self.char = bits[1]
        bits = self.full_char_range.split('-')
        self.min_count = int(bits[0])
        self.max_count = int(bits[1])

    def is_valid_one(self, text):
        occ = text.count(self.char)
        return self.min_count <= occ <= self.max_count

    def is_valid_two(self, text):
        chars = [text[i-1] == self.char for i in [self.min_count, self.max_count]]
        return any(chars) and not all(chars)

valid_pass_one = {
        True: 0,
        False: 0
}
valid_pass_two = {
        True: 0,
        False: 0
}

with open('input', 'r') as f:
    for line in f.readlines():
        pol, password = line.strip().split(':')
        password = password.strip()
        policy = Policy(pol)
        valid_pass_one[policy.is_valid_one(password)] += 1
        valid_pass_two[policy.is_valid_two(password)] += 1
print("one")
print(valid_pass_one)
print("two")
print(valid_pass_two)

