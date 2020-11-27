#!/usr/bin/env python3
f = open('input5.txt')
_in = 1
a = [int(x) for x in f.readline().split(',')]
def read(ar, val, mode):
    assert(0 <= mode <= 1)
    if mode == 0:
        return ar[val]
    elif mode == 1:
        return val
i = 0
while a[i] != 99:
    op, b = a[i] % 100, a[i] // 100
    mode1, b = b % 10, b // 10
    mode2, b = b % 10, b // 10

    if op == 1:
        a[a[i+3]] = read(a, a[i+1], mode1) + read(a, a[i+2], mode2)
        i += 4
    elif op == 2:
        a[a[i+3]] = read(a, a[i+1], mode1) * read(a, a[i+2], mode2)
        i += 4
    elif op == 3:
        a[a[i+1]] = _in
        i += 2
    elif op == 4:
        print(read(a, a[i+1], mode1))
        i += 2
