from collections import defaultdict
adjacents = [
    (x, y)
    for x in (-1, 0, 1)
    for y in (-1, 0, 1)
    if x != 0 or y != 0
]
class Position(object):
    @classmethod
    def build(cls, char, x, y):
        mapping = {
            kls.char: kls
            for kls in [
                Floor, EmptyChair, OccupiedChair
            ]
        }
        return mapping[char](x, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_adjacent_positions(self):
        for dx, dy in adjacents:
            yield self.x + dx, self.y + dy

    char = " "
    def __str__(self):
        return self.char

    def update(self, board):
        return None

class Floor(Position):
    char = "."

class EmptyChair(Position):
    char = "L"
    def update(self, board):
        occ = 0
        for x, y in self.get_adjacent_positions():
            if str(index_board(board, x, y)) == OccupiedChair.char:
                occ += 1
        if occ == 0:
            return OccupiedChair(self.x, self.y)

class OccupiedChair(Position):
    char = "#"
    def update(self, board):
        occupied = 0
        for x, y in self.get_adjacent_positions():
            if str(index_board(board, x, y)) == OccupiedChair.char:
                occupied += 1
        if occupied >= 4:
            return EmptyChair(self.x, self.y)

def update_board(board):
    changed = False
    new_board = [
        [
            None
            for char in line
        ]
        for line in board
        if line
    ]
    for y, row in enumerate(board):
        for x, position in enumerate(row):
            new_pos = position.update(board)
            if new_pos:
                changed = True
                position = new_pos
            new_board[y][x] = position
    return (new_board, changed)

def draw_board(board):
    for row in board:
        print("".join(str(pos) for pos in row))

def index_board(board, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return board[y][x]
    except IndexError:
        return None

with open('input', 'r') as f:
    all_data = f.read()
    board = [
        [
            Position.build(char, x, y)
            for x, char in enumerate(line)
        ]
        for y, line in enumerate(all_data.split("\n"))
        if line
    ]
just_changed = True
while just_changed:
    board, just_changed = update_board(board)

print("one")
print(sum([
    1
    for row in board
    for pos in row
    if str(pos) == "#"
]))
