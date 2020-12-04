passports = [[]]
for line in open('input4.txt').read().splitlines():
    if not line:
        passports.append([])
        continue
    for entry in line.split(' '):
        field, _ = entry.split(':')
        passports[-1].append(field)
print(sum(1 for valid_fields in passports if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(valid_fields)))
