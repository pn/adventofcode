#!/usr/bin/env python3
line = open('input11.txt').readline()
program = [int(x) for x in line.split(',')]


class State:
    def __init__(self, b, _in):
        self.a = [0 if x >= len(b) else b[x] for x in range(10 ** 5)]
        self.i = 0
        self.input = [_in]
        self.output = []
        self.base = 0
        self.modes = {}

    def read(self, offset):
        mode, val = self.modes[offset], self.a[self.i + offset]
        assert (0 <= mode <= 2)
        if mode == 0:
            return self.a[val]
        elif mode == 1:
            return val
        elif mode == 2:
            return self.a[self.base + val]

    def save(self, offset, val):
        base = self.base if self.modes[offset] == 2 else 0
        self.a[base + self.a[self.i + offset]] = val

    def run(self):
        while self.a[self.i] != 99:
            op, b = self.a[self.i] % 100, self.a[self.i] // 100
            self.modes[1], b = b % 10, b // 10
            self.modes[2], b = b % 10, b // 10
            self.modes[3], b = b % 10, b // 10
            arg1 = self.read(1)
            arg2 = self.read(2) if op not in [3, 4, 9] else None
            if op == 1:
                self.save(3, arg1 + arg2)
                self.i += 4
            elif op == 2:
                self.save(3, arg1 * arg2)
                self.i += 4
            elif op == 3:
                self.save(1, self.input.pop(0))
                self.i += 2
            elif op == 4:
                self.i += 2
                self.output.append(arg1)
                return True
            elif op == 5:
                self.i = arg2 if arg1 else self.i + 3
            elif op == 6:
                self.i = arg2 if not arg1 else self.i + 3
            elif op == 7:
                self.save(3, 1 if arg1 < arg2 else 0)
                self.i += 4
            elif op == 8:
                self.save(3, 1 if arg1 == arg2 else 0)
                self.i += 4
            elif op == 9:
                self.base += arg1
                self.i += 2
        return False


def get_colors(starting_color):
    state = State(program.copy(), starting_color)
    colors = {}
    pos = (0, 0)
    direction = 0
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while state.run():
        color = state.output.pop(0)
        colors[pos] = color
        state.run()
        direction = (direction + (1 if state.output.pop(0) == 1 else len(directions) - 1)) % len(directions)
        pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        state.input.append(colors.get(pos, 0))
    return colors


def render_colors(colors):
    xs = list(map(lambda x: x[0], colors.keys()))
    ys = list(map(lambda x: x[1], colors.keys()))
    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)
    print(min_x, min_y, max_x, max_y)
    for j in range(max_y - min_y + 1):
        row = ''
        for i in range(max_x - min_x + 1):
            row = row + ('*' if colors.get((i, j), 0) else ' ')
        print(row)


print(len(get_colors(0)))
render_colors(get_colors(1))
