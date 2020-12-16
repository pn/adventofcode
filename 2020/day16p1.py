lines = [line for line in open('input16.txt').read().splitlines() if line]
i = 0
rules = []
for i, line in enumerate(lines):
    if line.startswith('your ticket:'):
        break
    rules.append(list(list(int(r) for r in rule.split('-')) for rule in line.split(': ')[1].split(' or ')))
tickets = []
for line in lines[i + 3:]:
    tickets.append(tuple(int(l) for l in line.split(',')))

def valid(value: int):
    return any(range[0] <= value <= range[1] for rule in rules for range in rule)

print(sum(value for ticket in tickets for value in ticket if not(valid(value))))
