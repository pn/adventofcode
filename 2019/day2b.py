#!/usr/bin/env python3
f = open('input2.txt')
line = f.readline()
b = [int(x) for x in line.split(',')]
for noun in range(100):
    for verb in range(100):
        a = b.copy()
        a[1] = noun
        a[2] = verb
        ops = 0
        i = 0
        while a[i] != 99:
            if a[i] == 1:
                a[a[i+3]] = a[a[i+1]] + a[a[i+2]]
                i += 4
                ops+=1
            elif a[i] == 2:
                a[a[i+3]] = a[a[i+1]] * a[a[i+2]]
                i += 4
                ops+=1
            else: raise ValueError()
        if a[0] == 19690720:
            print(f'found it: {verb} {noun}')
            print(100 * noun + verb)
