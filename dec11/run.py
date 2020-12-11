from collections import defaultdict
adjacents = [
    (x, y)
    for x in (-1, 0, 1)
    for y in (-1, 0, 1)
    if x != 0 or y != 0
]

class Board(object):
    def __init__(self, path, look=1):
        self.path = path
        self.look = look
        self.board_data = self.load(path)

    def update(self):
        changed = False
        new_board = [
            [
                None
                for char in line
            ]
            for line in self.board_data
            if line
        ]
        for y, row in enumerate(self.board_data):
            for x, position in enumerate(row):
                new_pos = position.update(self)
                if new_pos:
                    changed = True
                    position = new_pos
                new_board[y][x] = position
        self.board_data = new_board
        return (self, changed)

    def draw(self):
        print('-----------')
        for row in self.board_data:
            print("".join(str(pos) for pos in row))

    def index(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.board_data[y][x]
        except:
            return None

    def load(self, path):
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
        return board
    def run(self):
        just_changed = True
        while just_changed:
            self, just_changed = self.update()
        return self

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

    def count_seen_chairs(self, direction, board):
        (x, y) = direction
        for distance in range(1, board.look):
            nx = self.x + (x * distance)
            ny = self.y + (y * distance)
            pos = str(board.index(nx, ny))
            if pos == EmptyChair.char:
                return 0
            elif pos == OccupiedChair.char:
                return 1
        return 0

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
        for direction in adjacents:
            occ += self.count_seen_chairs(direction, board)
        if occ == 0:
            return OccupiedChair(self.x, self.y)

class OccupiedChair(Position):
    char = "#"
    def update(self, board):
        occupied = 0
        for direction in adjacents:
            occupied += self.count_seen_chairs(direction, board)
        if occupied >= 5:
            return EmptyChair(self.x, self.y)

board = Board('input', 500).run()
num = sum([
    1
    for row in board.board_data
    for pos in row
    if str(pos) == "#"
])
print(num)
