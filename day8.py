#!/usr/bin/env python3
size, s = 25 * 6, open('input8.txt').readline().strip()
layers = [s[i:i + size] for i in range(0, len(s), size)]
out = list(layers[0])
for layer in layers:
    for i in range(len(layer)):
        if out[i] == '2':
            out[i] = layer[i]
for row in [out[i:i + 25] for i in range(0, len(out), 25)]:
    print(''.join(row).replace('0', ' ').replace('1', '*'))
