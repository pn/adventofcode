valid = 0
for line in open('input2.txt'):
    parts = line.split(' ')
    l_min = int(parts[0].split('-')[0])
    l_max = int(parts[0].split('-')[1])
    letter = parts[1][0]
    password = parts[2].strip('\n')
    if password.count(letter) in range(l_min, l_max + 1):
        valid += 1
print(valid)
