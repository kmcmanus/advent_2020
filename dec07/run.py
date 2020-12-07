
class ChildBag(object):
    def __init__(self, line):
        bits = line.split()
        self.quantity = int(bits[0])
        self.bag = " ".join(bits[1:])

    def __str__(self):
        return f"{self.quantity} {self.bag}"
class Rule(object):
    def __init__(self, line):
        self.line = line
        self.process_line(line)

    def process_line(self, line):
        bits = line.split(" contain ")
        self.bag = bits[0]
        if bits[1] == "no other bags.":
            self.children = []
        else:
            children_bits = bits[1].rstrip(".").split(", ")
            self.children = list(map(ChildBag, children_bits))

    def __str__(self):
        return f"{self.bag} contains {', '.join(map(str, self.children))}."

with open('input', 'r') as f:
    all_data = f.read()
    rules = [
        Rule(line.strip())
        for line in all_data.split("\n")
        if line
    ]
rule_by_bag = {
        r.bag: r.children
        for r in rules
        }

def can_contain(parent_bag, child_bag, so_far=[]):


print(rule_by_bag)
