orig_code = []
for line in open('input8.txt').read().splitlines():
    _op, _arg = line.split(' ')
    orig_code.append([_op, int(_arg)])

def run(code):
    acc = i = 0
    ran = set()
    while i not in ran and i < len(code):
        ran.add(i)
        op, arg = code[i]
        if op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        else:
            i += 1
    if i >= len(code):
        return acc
    return None

for j in range(len(orig_code)):
    code = orig_code.copy()
    op, arg = code[j]
    if op == 'jmp':
        code[j] = ['nop', arg]
    elif op == 'nop':
        code[j] = ['jmp', arg]
    else:
        continue
    result = run(code)
    if result is not None:
        print(result)
