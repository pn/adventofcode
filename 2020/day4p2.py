import re
passports = [[]]
for line in open('input4.txt').read().splitlines():
    if not line:
        passports.append([])
        continue
    for entry in line.split(' '):
        field, value = entry.split(':')
        if field == 'byr' and 1920 <= int(value) <= 2002 or \
                field == 'iyr' and 2010 <= int(value) <= 2020 or \
                field == 'eyr' and 2020 <= int(value) <= 2030 or \
                field == 'hgt' and (value.endswith('cm') and 150 <= int(value.rstrip('cm')) <= 193 or
                                    value.endswith('in') and 59 <= int(value.rstrip('in')) <= 76) or \
                field == 'hcl' and re.match(r'^#[0-9a-z]{6}$', value) or \
                field == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or \
                field == 'pid' and re.match(r'^[0-9]{9}$', value):
            passports[-1].append(field)
print(sum(1 for valid_fields in passports if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(valid_fields)))
