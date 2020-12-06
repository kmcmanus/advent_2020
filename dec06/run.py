from functools import reduce

class Declaration(object):
    def __init__(self, line):
        self.line = line
        self.answers = [set(l.strip()) for l in line.split()]

    def superset_answers(self):
        return set([
            char
            for answer in self.answers
            for char in answer
            ])

    def intersection_answers(self):
        return reduce(lambda s, o: s.intersection(o), self.answers)

assert Declaration("ab\nac").answers == [set("ab"), set("ac")]
assert Declaration("ab\nac").superset_answers() == set(["a", "b", "c"])
assert Declaration("ab\nac").intersection_answers() == set(["a"])

declarations = []
with open('input', 'r') as f:
    all_data = f.read()
    declarations = [
        Declaration(line.strip())
        for line in all_data.split("\n\n")
    ]
print("one")
print(sum([
    len(declaration.superset_answers())
    for declaration in declarations
]))

print("two")
print(sum([
    len(declaration.intersection_answers())
    for declaration in declarations
]))

