valid = 0
for line in open('input2.txt'):
    parts = line.split(' ')
    first = int(parts[0].split('-')[0])
    second = int(parts[0].split('-')[1])
    letter = parts[1][0]
    password = parts[2].strip('\n')
    if (password[first-1] == letter) != (password[second-1] == letter):
        valid += 1
print(valid)
