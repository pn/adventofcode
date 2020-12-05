seats = []
for line in open('input5.txt').read().splitlines():
    row = column = 0
    for c in line[:7]:
        row *= 2
        if c == 'B':
            row += 1
    for c in line[7:]:
        column *= 2
        if c == 'R':
            column += 1
    seats.append(8 * row + column)
seats = sorted(seats)
print(f'part1 {seats[-1]}')
for i in range(0, len(seats) - 1):
    if seats[i + 1] - seats[i] == 2:
        print(f'part2 {seats[i] + 1}')

# compressed

seats = []
for line in open('input5.txt').read().splitlines():
    row = sum(2**i for i, c in enumerate(line[6::-1]) if c == 'B')
    column = sum(2**i for i, c in enumerate(line[:-4:-1]) if c == 'R')
    seats.append(8 * row + column)
seats = sorted(seats)
print(f'part1 {seats[-1]}')
print(f'part2 {[i for i in range(0, len(seats) - 1) if seats[i + 1] - seats[i] == 2][0]}')

# alternative

seats = []
for line in open('input5.txt').read().splitlines():
    row = int(line[:7].replace('B', '1').replace('F', '0'), 2)
    column = int(line[7:].replace('R', '1').replace('L', '0'), 2)
    seats.append(8 * row + column)
seats = sorted(seats)
print(f'part1 {seats[-1]}')
print(f'part2 {[i for i in range(0, len(seats) - 1) if seats[i + 1] - seats[i] == 2][0]}')
