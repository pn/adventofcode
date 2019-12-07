#!/usr/bin/env python3
import itertools
line = open('input7.txt').readline()
i, a = 0, [int(x) for x in line.split(',')]


def read(ar, val, mode):
    assert(0 <= mode <= 1)
    return ar[val] if mode == 0 else val


def run(prog, _in):
    i = 0
    a = prog.copy()
    while a[i] != 99:
        op, b = a[i] % 100, a[i] // 100
        mode1, b = b % 10, b // 10
        mode2, b = b % 10, b // 10
        arg1 = read(a, a[i+1], mode1)
        arg2 = read(a, a[i+2], mode2) if op not in [3, 4] else None
        if op == 1:
            a[a[i+3]] = arg1 + arg2
            i += 4
        elif op == 2:
            a[a[i+3]] = arg1 * arg2
            i += 4
        elif op == 3:
            a[a[i+1]] = _in.pop(0)
            i += 2
        elif op == 4:
            i += 2
            return arg1
        elif op == 5:
            i = arg2 if arg1 else i + 3
        elif op == 6:
            i = arg2 if not arg1 else i + 3
        elif op == 7:
            a[a[i+3]] = 1 if arg1 < arg2 else 0
            i += 4
        elif op == 8:
            a[a[i+3]] = 1 if arg1 == arg2 else 0
            i += 4


outputs = []
for perm in list(itertools.permutations(range(5))):
    out = i
    for p in range(5):
        out = run(a, [perm[p], out])
    outputs.append(out)
print(max(outputs))
