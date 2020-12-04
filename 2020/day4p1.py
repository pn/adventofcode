lines = open('input4.txt').read().splitlines()
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
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
        passport[key] = value

passports.append(passport)
valid = 0
for passport in passports:
    if set(set(fields)).issubset(passport.keys()):
        valid += 1
print(valid)
