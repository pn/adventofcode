valid = 0
for line in open('input2.txt'):
    parts = line.strip('\n').split(' ')
    l_min, l_max = [int(part) for part in parts[0].split('-')]
    letter, password = parts[1][0], parts[2]
    if password.count(letter) in range(l_min, l_max + 1):
        valid += 1
print(valid)
