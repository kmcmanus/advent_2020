class InfiniteLoopDetected(BaseException):
    def __init__(self, step, accumulator, program):
        self.step = step
        self.accumulator = accumulator
        self.program = program

class Operation(object):
    def __init__(self, value):
        self.value = value
        self.visits = 0

    @classmethod
    def load(cls, line):
        (op, amt) = line.split()
        klass = {
            "nop": NoOp,
            "jmp": Jump,
            "acc": Accumulate
        }[op]
        return klass(int(amt))

    def step(self, current_step, accumulator, program):
        if self.visits > 0:
            raise InfiniteLoopDetected(self, accumulator, program)
        self.visits += 1
        return (current_step, accumulator)


class NoOp(Operation):
    def step(self, current_step, accumulator, program):
        super().step(current_step, accumulator, program)
        return (current_step + 1, accumulator)

class Jump(Operation):
    def step(self, current_step, accumulator, program):
        super().step(current_step, accumulator, program)
        return (current_step + self.value, accumulator)

class Accumulate(Operation):
    def step(self, current_step, accumulator, program):
        super().step(current_step, accumulator, program)
        return (current_step + 1, accumulator + self.value)

def execute(program):
    current_step = 0
    accumulator = 0
    while current_step < len(program):
        (current_step, accumulator) = program[current_step].step(
                current_step,
                accumulator,
                program
        )
    return accumulator

with open('input', 'r') as f:
    all_data = f.read()
    tokens = [
        Operation.load(line.strip())
        for line in all_data.split("\n")
        if line
    ]
print("one")
try:
    execute(tokens)
except InfiniteLoopDetected as i:
    print(i.accumulator)

print("two")
print(count("shiny gold bag", rule_by_bag))
