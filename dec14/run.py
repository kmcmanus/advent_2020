import functools
import re
import collections
class Mask(object):
    def __init__(self, line):
        self.line = line

    def apply(self, state):
        return {
            "current_mask": self,
            "memory": state["memory"]
        }

    @classmethod
    def applies(cls, line):
        if line.startswith("mask = "):
            return cls(line.lstrip("mask = "))
        return None

mem_reg = r"^mem\[([0-9]+)\] = ([0-9]+)$"
class MemSet(object):
    def __init__(self, key, value):
        self.key = int(key)
        self.value = int(value)

    def apply(self, state):
        def mask_char(mask, val):
            if mask == "X":
                return val
            return mask
        new_val = [
                mask_char(mask, val)
                for mask, val in zip(
                    state["current_mask"].line,
                    f"{self.value:032b}"
                )
            ]
        state["memory"][self.key] = int("".join(new_val), 2)
        return state

    @classmethod
    def applies(cls, line):
        match = re.match(mem_reg, line)
        if match:
            (key, value) = match.groups()
            return cls(key, value)
        return None
klasses = [Mask, MemSet]
def load(path='input'):
    with open(path, 'r') as f:
        for line in f.readlines():
            for kls in [Mask, MemSet]:
                data = kls.applies(line)
                if data:
                    yield data

data = list(load())

state = {
    "current_mask": None,
    "memory": collections.defaultdict(int)
}
state = functools.reduce(lambda state, d: d.apply(state), data, state)
print("one")
print(functools.reduce(lambda x, y: x + y, state["memory"].values()))
