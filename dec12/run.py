import functools
import math


def north(length, x, y, facing):
    return {
            "x": x,
            "y": y + length,
            "facing": facing
        }

def south(length, x, y, facing):
    return {
            "x": x,
            "y": y - length,
            "facing": facing
         }

def east(length, x, y, facing):
    return {
            "x": x + length,
            "y": y,
            "facing": facing
        }

def west(length, x, y, facing):
    return {
            "x": x - length,
            "y": y,
            "facing": facing
        }

def right(length, x, y, facing):
    return {
            "x": x,
            "y": y,
            "facing": facing + length
        }

def left (length, x, y, facing):
    return {
            "x": x,
            "y": y,
            "facing": facing - length
        }

def forward(length, x, y, facing):
    return {
            "x": round(x + math.cos(math.radians(facing)) * length),
            "y": round(y - math.sin(math.radians(facing)) * length),
            "facing": facing
        }

def wp_north(length, x, y, wp_x, wp_y):
    return {
            "x": x,
            "y": y,
            "wp_x": wp_x,
            "wp_y": wp_y + length,
        }

def wp_south(length, x, y, wp_x, wp_y):
    return {
            "x": x,
            "y": y,
            "wp_x": wp_x,
            "wp_y": wp_y - length,
         }

def wp_east(length, x, y, wp_x, wp_y):
    return {
            "x": x,
            "y": y,
            "wp_x": wp_x + length,
            "wp_y": wp_y,
        }

def wp_west(length, x, y, wp_x, wp_y):
    return {
            "x": x,
            "y": y,
            "wp_x": wp_x - length,
            "wp_y": wp_y,
        }

def wp_right(length, x, y, wp_x, wp_y):
    length = length if length == 180 else (length + 180) % 360
    return wp_left(length, x, y, wp_x, wp_y)

def wp_left(length, x, y, wp_x, wp_y):
    rads = math.radians(length)
    cos = math.cos(rads)
    sin = math.sin(rads)
    return {
            "x": x,
            "y": y,
            "wp_x": round((cos * wp_x) - (sin * wp_y)),
            "wp_y": round((sin * wp_x) + (cos * wp_y)),
        }

def wp_forward(length, x, y, wp_x, wp_y):
    return {
            "x": x + (wp_x * length),
            "y": y + (wp_y * length),
            "wp_x": wp_x,
            "wp_y": wp_y,
        }

instructions = {
    "N": north,
    "S": south,
    "E": east,
    "W": west,
    "L": left,
    "R": right,
    "F": forward
}

wp_instructions = {
    "N": wp_north,
    "S": wp_south,
    "E": wp_east,
    "W": wp_west,
    "L": wp_left,
    "R": wp_right,
    "F": wp_forward
}

def load(instructions):
    with open('input') as f:
        return [
            functools.partial(instructions[line[0]], length=int(line[1:].strip()))
            for line in f.readlines()
            if line
        ]
def execute(data, func):
    print('---')
    print(data)
    print(func)
    return func(**data)
start = {
    "x": 0,
    "y": 0,
    "facing": 0
}
result = functools.reduce(lambda data, func: func(**data), load(instructions), start)
print("one")
print(abs(result["x"]) + abs(result["y"]))

start = {
    "x": 0,
    "y": 0,
    "wp_x": 10,
    "wp_y": 1,
}

result = functools.reduce(lambda data, func: func(**data), load(wp_instructions), start)
print(result)
print("two")
print(abs(result["x"]) + abs(result["y"]))
