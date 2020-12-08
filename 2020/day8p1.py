code = []
for line in open('input8.txt').read().splitlines():
    cmd, arg = line.split(' ')
    code.append((cmd, int(arg)))

acc = i = 0
ran = set()
while i not in ran:
    ran.add(i)
    op, arg = code[i]
    if op == 'acc':
        acc += arg
        i += 1
    elif op == 'jmp':
        i += arg
    else:
        i += 1
print(acc)
