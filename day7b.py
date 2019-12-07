#!/usr/bin/env python3
from itertools import permutations
line = open('input7.txt').readline()
i, a = 0, [int(x) for x in line.split(',')]


def read(ar, val, mode):
    assert(0 <= mode <= 1)
    return ar[val] if mode == 0 else val


class State:
    def __init__(self, b, phase):
        self.a = b.copy()
        self.i = 0
        self.input = [phase]
        self.output = []


def run(s: State):
    while a[s.i] != 99:
        op, b = a[s.i] % 100, a[s.i] // 100
        mode1, b = b % 10, b // 10
        mode2, b = b % 10, b // 10
        arg1 = read(a, a[s.i+1], mode1)
        arg2 = read(a, a[s.i+2], mode2) if op not in [3, 4] else None
        if op == 1:
            a[a[s.i+3]] = arg1 + arg2
            s.i += 4
        elif op == 2:
            a[a[s.i+3]] = arg1 * arg2
            s.i += 4
        elif op == 3:
            a[a[s.i+1]] = s.input.pop(0)
            s.i += 2
        elif op == 4:
            s.i += 2
            s.output.append(arg1)
            return False
        elif op == 5:
            s.i = arg2 if arg1 else s.i + 3
        elif op == 6:
            s.i = arg2 if not arg1 else s.i + 3
        elif op == 7:
            a[a[s.i+3]] = 1 if arg1 < arg2 else 0
            s.i += 4
        elif op == 8:
            a[a[s.i+3]] = 1 if arg1 == arg2 else 0
            s.i += 4
    return True


outputs = []
for perm in list(permutations(range(5, 10))):
    n, states = 0, [State(a, perm[p]) for p in range(5)]
    states[n].input.append(0)
    while True:
        if run(states[n]):
            outputs.append(states[n].input[-1])
            break
        else:
            states[(n + 1) % 5].input.append(states[n].output.pop(0))
        n = (n + 1) % 5
print(max(outputs))
