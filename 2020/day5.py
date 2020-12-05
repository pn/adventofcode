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
