lines = [line for line in open('input16.txt').read().splitlines() if line]
i = 0
rules = []
rule_names = []
for i, line in enumerate(lines):
    if line.startswith('your ticket:'):
        break
    rule_names.append(line.split(': ')[0])
    rules.append(list(list(int(r) for r in rule.split('-')) for rule in line.split(': ')[1].split(' or ')))
i += 1
my_ticket = tuple(int(l) for l in lines[i].split(','))
tickets = []
for line in lines[i + 2:]:
    tickets.append(tuple(int(l) for l in line.split(',')))

def matches_rule(rule, value):
    return any(range[0] <= value <= range[1] for range in rule)

def valid_field(value: int):
    return any(matches_rule(rule, value) for rule in rules)

def valid_ticket(ticket):
    return all(valid_field(value) for value in ticket)

def possible_fields(ticket):
    result = []
    for value in ticket:
        result.append([])
        for i, rule in enumerate(rules):
            if matches_rule(rule, value):
                result[-1].append(rule_names[i])
    return result

possibilities = [possible_fields(ticket) for ticket in tickets if valid_ticket(ticket)]
common_possibilities = []
for i in range(len(my_ticket)):
    common = set()
    for possibility in possibilities:
        if common:
            common = common.intersection(set(possibility[i]))
        else:
            common = set(possibility[i])

    common_possibilities.append(common)

left = rule_names.copy()
while left:
    for j, common in enumerate(common_possibilities):
        if len(common) == 1 and list(common)[0] in left:
            name = list(common)[0]
            left.remove(name)
            for i, c in enumerate(common_possibilities):
                if i != j and name in list(common_possibilities[i]):
                    common_possibilities[i].remove(name)
            break

result = 1
for i, c in enumerate(common_possibilities):
    name = list(c)[0]
    if 'departure' in name:
        result *= my_ticket[i]
print(result)
