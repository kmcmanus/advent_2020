class InfiniteLoopDetected(BaseException):
    def __init__(self, step, accumulator):
        self.step = step
        self.accumulator = accumulator

class Program(object):
    def __init__(self, path='input'):
        self.path = path
        self.reload()

    def reload(self):
        with open(self.path, 'r') as f:
            all_data = f.read()
            program = [
                Operation.load(line.strip())
                for line in all_data.split("\n")
                if line
            ]
            self.steps = program

    def execute(self):
        program = list(map(lambda s: s.reset(), self.steps))
        current_step = 0
        accumulator = 0
        while current_step < len(program):
            (current_step, accumulator) = program[current_step].step(
                    current_step,
                    accumulator,
                    program
            )
        return accumulator

class Operation(object):
    def __init__(self, operation, value):
        self.value = value
        self.visits = 0
        self.operation = operation

    def reset(self):
        self.visits = 0
        return self

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


print("one")
program = Program()
try:
    res = program.execute()
except InfiniteLoopDetected as i:
    print(i.accumulator)

print("two")
for (i, step) in enumerate(program.steps):
    if step.operation == 'acc':
        continue
    program.steps[i] = program.steps[i].invert()
    try:
        acc = program.execute()
    except InfiniteLoopDetected as ex:
        program.steps[i] = program.steps[i].invert()
        continue
    print("won!")
    print(acc)
    break


