#!/usr/bin/env python3
min0, ml, s = 25 * 6, None, open('input8.txt').readline().strip()
for layer in [s[i:i + min0] for i in range(0, len(s), min0)]:
    if layer.count('0') < min0:
        min0 = layer.count('0')
        ml = layer
print(ml.count('1') * ml.count('2'))
