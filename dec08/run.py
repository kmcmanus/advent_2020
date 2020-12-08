import copy
class InfiniteLoopDetected(BaseException):
    def __init__(self, step, accumulator):
        self.step = step
        self.accumulator = accumulator

class Operation(object):
    def __init__(self, operation, value):
        self.value = value
        self.visits = 0
        self.operation = operation

    @classmethod
    def load(cls, line):
        (op, amt) = line.split()
        klass = {
            "nop": NoOp,
            "jmp": Jump,
            "acc": Accumulate
        }[op]
        return klass(op, int(amt))

    def step(self, current_step, accumulator, program):
        if self.visits > 0:
            raise InfiniteLoopDetected(self, accumulator)
        self.visits += 1
        return (current_step, accumulator)


class NoOp(Operation):
    def step(self, current_step, accumulator, program):
        super().step(current_step, accumulator, program)
        return (current_step + 1, accumulator)
    def invert(self):
        return Jump("jmp", self.value)

class Jump(Operation):
    def step(self, current_step, accumulator, program):
        super().step(current_step, accumulator, program)
        return (current_step + self.value, accumulator)
    def invert(self):
        return NoOp("nop", self.value)

class Accumulate(Operation):
    def step(self, current_step, accumulator, program):
        super().step(current_step, accumulator, program)
        return (current_step + 1, accumulator + self.value)

def clone(program):
    return list(map(copy.copy, program))

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
    program = [
        Operation.load(line.strip())
        for line in all_data.split("\n")
        if line
    ]
print("one")
try:
    execute(program)
except InfiniteLoopDetected as i:
    print(i.accumulator)

print("two")
for (i, step) in enumerate(program):
    if step.operation == 'acc':
        continue
    temp_prog = clone(program)
    print(temp_prog[i])
    temp_prog[i] = temp_prog[i].invert()
    print(temp_prog[i])
    try:
        acc = execute(temp_prog)
    except InfiniteLoopDetected as ex:
        print(i, ex)
        continue
    print(acc)
    break


