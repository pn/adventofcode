#!/usr/bin/env python3
import re
a,b = '156218-652527'.split('-')
reg = re.compile(r'(\d)\1')
reg2 = re.compile(r'(\d)\1\1')
result = 0
for i in range(int(a), int(b)+1):
    s = str(i)
    if ''.join(sorted(s)) != s:
        continue
    if not reg.search(s):
        continue
    if set(reg2.findall(s)) == set(reg.findall(s)):
        continue
    result+=1
print(result)
