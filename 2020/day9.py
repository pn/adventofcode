import sys

numbers = []
previous = 25
for line in open('input9.txt').read().splitlines():
    numbers.append(int(line))

last_numbers = numbers[:previous]
found = None
for i in range(previous, len(numbers)):
    number = numbers[i]
    valid = False
    for n in last_numbers:
        if number - n in last_numbers:
            valid = True
            break
    if not valid:
        found = number
        break
    last_numbers.append(number)
    last_numbers.pop(0)
print(f'part1 {found}')

for i in range(len(numbers)):
    s = 0
    for j in range(i, len(numbers)):
        s += numbers[j]
        if s == found:
            print(f'part2 {max(numbers[i:j]) + min(numbers[i:j])}')
            sys.exit(0)
