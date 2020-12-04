import re

lines = open('input4.txt').read().splitlines()
fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', ]
passports = []
passport = {}
for line in lines:
    if not line:
        if passport:
            passports.append(passport)
            passport = {}
        continue

    line_entries = line.split(' ')
    for entry in line_entries:
        key, value = entry.split(':')
        if key == 'byr' and (1920 <= int(value) <= 2002):
            passport[key] = value
        elif key == 'iyr' and (2010 <= int(value) <= 2020):
            passport[key] = value
        elif key == 'eyr' and (2020 <= int(value) <= 2030):
            passport[key] = value
        elif key == 'hgt':
            if value.endswith('cm'):
                v = value.rstrip('cm')
                if 150 <= int(v) <= 193:
                    passport[key] = value
            elif value.endswith('in'):
                v = value.rstrip('in')
                if 59 <= int(v) <= 76:
                    passport[key] = value
        elif key == 'hcl' and (re.match(r"#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]", value)):
            passport[key] = value
        elif key == 'ecl' and (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            passport[key] = value
        elif key == 'pid' and (len(value) == 9):
            try:
                passport[key] = int(value)
            except ValueError:
                pass

passports.append(passport)
valid = 0
for passport in passports:
    if set(set(fields)).issubset(passport.keys()):
        valid += 1

print(valid)
