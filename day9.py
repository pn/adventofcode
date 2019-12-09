#!/usr/bin/env python3
line = open('input9.txt').readline()
program = [int(x) for x in line.split(',')]


def read(ar, val, mode, base):
    assert(0 <= mode <= 2)
    if mode == 0:
        return ar[val]
    elif mode == 1:
        return val
    elif mode == 2:
        return ar[base + val]


class State:
    def __init__(self, b, _in):
        self.a = [0 if x >= len(b) else b[x] for x in range(10**5)]
        self.i = 0
        self.input = [_in]
        self.output = []
        self.base = 0

    def save(self, offset, val, modes):
        base = self.base if modes[offset] == 2 else 0
        self.a[base + self.a[self.i + offset]] = val


def run(s: State):
    modes = {}
    while s.a[s.i] != 99:
        op, b = s.a[s.i] % 100, s.a[s.i] // 100
        modes[1], b = b % 10, b // 10
        modes[2], b = b % 10, b // 10
        modes[3], b = b % 10, b // 10
        arg1 = read(s.a, s.a[s.i+1], modes[1], s.base)
        arg2 = read(s.a, s.a[s.i+2], modes[2], s.base) if op not in [3, 4, 9] else None
        if op == 1:
            s.save(3, arg1 + arg2, modes)
            s.i += 4
        elif op == 2:
            s.save(3, arg1 * arg2, modes)
            s.i += 4
        elif op == 3:
            s.save(1, s.input.pop(0), modes)
            s.i += 2
        elif op == 4:
            s.i += 2
            s.output.append(arg1)
        elif op == 5:
            s.i = arg2 if arg1 else s.i + 3
        elif op == 6:
            s.i = arg2 if not arg1 else s.i + 3
        elif op == 7:
            s.save(3, 1 if arg1 < arg2 else 0, modes)
            s.i += 4
        elif op == 8:
            s.save(3, 1 if arg1 == arg2 else 0, modes)
            s.i += 4
        elif op == 9:
            s.base += arg1
            s.i += 2
    return True


s = State(program, 1)
run(s)
print(s.output[-1])
