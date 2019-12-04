#!/usr/bin/env python3
result = 0
with open('input1.txt') as f:
    for line in f:
        result += int(line) // 3 - 2
print(result)
