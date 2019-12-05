#!/usr/bin/env python3
i, _in, a = 0, 5, [int(x) for x in open('input5.txt').readline().split(',')]
def read(ar, val, mode):
    assert(0 <= mode <= 1)
    return ar[val] if mode == 0 else val
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
        a[a[i+1]] = _in
        i += 2
    elif op == 4:
        print(arg1)
        i += 2
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
