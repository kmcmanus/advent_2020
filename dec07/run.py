
def bag_name(name):
    return name.replace("bags", "bag")

class ChildBag(object):
    def __init__(self, line):
        bits = line.split()
        self.count = int(bits[0])
        self.bag = bag_name(" ".join(bits[1:]))

    def __str__(self):
        return f"{self.count} {self.bag}"
class Rule(object):
    def __init__(self, line):
        self.line = line
        self.process_line(line)

    def process_line(self, line):
        bits = line.split(" contain ")
        self.bag = bag_name(bits[0])
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
children_by_bag = {
        r.bag: [c.bag for c in r.children]
        for r in rules
        }
rule_by_bag = {
        r.bag: r
        for r in rules
        }

def traverse(bag, tree):
    results = []
    for child in tree.get(bag, []):
        results.append(child)
        results.extend(traverse(child, tree))
    return results

traversed_bags = {
        r.bag: traverse(r.bag, children_by_bag)
        for r in rules
        }
print("one")
print(sum([
    1
    for (bag, kids) in traversed_bags.items()
    if "shiny gold bag" in kids
]))

memo = {}
def count(bag, tree):
    results = 0
    for child in tree.get(bag, []).children:
        recurse = memo.get(child.bag, count(child.bag, tree))
        results += child.count + child.count * recurse
        memo[child.bag] = recurse
    return results
print("two")
print(count("shiny gold bag", rule_by_bag))
