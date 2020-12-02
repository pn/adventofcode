valid = 0
for line in open('input2.txt'):
    parts = line.strip('\n').split(' ')
    first, second = [int(part) for part in parts[0].split('-')]
    letter, password = parts[1][0], parts[2]
    if (password[first-1] == letter) != (password[second-1] == letter):
        valid += 1
print(valid)
