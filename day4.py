#!/usr/bin/env python3
import re
a,b = '156218-652527'.split('-')
reg = re.compile(r'(\d)\1')
result = 0
for i in range(int(a), int(b)+1):
    if ''.join(sorted(str(i))) != str(i):
        continue
    if not reg.search(str(i)):
        continue
    result+=1
print(result)
