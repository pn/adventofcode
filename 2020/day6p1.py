from string import ascii_lowercase

groups = [[]]
for line in open('input6.txt').read().splitlines():
    if not line:
        groups.append([])
        continue
    groups[-1].append(line)

total = 0
for group in groups:
    i = 0
    answers = ''.join(group)
    for letter in ascii_lowercase:
        if letter in answers:
            i += 1
    total += i

print(total)
