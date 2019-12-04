#!/usr/bin/env python3
result = 0
with open('input1.txt') as f:
    for line in f:
        r = int(line) // 3 - 2
        if r > 0:
            result += r
        else:
            print('wat?')
        while(r > 0):
            r = r // 3 - 2
            if r <= 0:
                continue
            result += r
print(result)
