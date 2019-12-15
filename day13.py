#!/usr/bin/env python3
line = open('input13.txt').readline()
program = [int(x) for x in line.split(',')]
screen = {}


class State:
    def __init__(self, b, _in=None):
        self.a = [0 if x >= len(b) else b[x] for x in range(10 ** 5)]
        self.i = 0
        self.input = [_in] if _in else []
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
                return self.output[-1]
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
        return None


def play(program, screen):
    s = State(program)
    while True:
        x = s.run()
        if x is None:
            return
        y = s.run()
        t = s.run()
        screen[(x, y)] = t


play(program, screen)
count = 0
for tile in screen.values():
    if tile == 2:
        count += 1
print(count)
