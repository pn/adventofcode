#!/usr/bin/env python3
f = open('input2.txt')
line = f.readline()
a = [int(x) for x in line.split(',')]
#print(a)
i = 0
#print(a)
a[1] = 12
a[2] = 2
#print(a)
while a[i] != 99:
    #print(f'pos {i}')
    if a[i] == 1:
        pos1, pos2, respos = a[i+1], a[i+2], a[i+3]
        a[a[i+3]] = a[a[i+1]] + a[a[i+2]]
        # a[i+3] = a[i+1] + a[i+2]
        i += 4
    elif a[i] == 2:
        # a[i+3] = a[i+1] * a[i+2]
        a[a[i+3]] = a[a[i+1]] * a[a[i+2]]
        i += 4
    else: raise ValueError()
    #print(a)

print(a[0])
