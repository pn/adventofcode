rows = [line for line in open('input11.txt').read().splitlines()]
rows2 = rows.copy()

def occupied(rows, x, y, one):
    result = 0
    directions = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
    directions.remove((0, 0))
    for direction in directions:
        pos_x = x + direction[1]
        pos_y = y + direction[0]
        while True:
            if pos_x < 0 or pos_x >= len(rows[0]) or pos_y < 0 or pos_y >= len(rows):
                break
            seat = rows[pos_y][pos_x]
            if seat == '#':
                result += 1
                break
            elif seat == 'L':
                break
            elif one:
                break
            pos_x += direction[1]
            pos_y += direction[0]
    return result

def run(rows, one=False):
    while True:
        changes = []
        for j, row in enumerate(rows):
            for i, seat in enumerate(row):
                o = occupied(rows, i, j, one)
                if seat == 'L' and o == 0:
                    changes.append((i, j, '#'))
                elif seat == '#' and o >= (4 if one else 5):
                    changes.append((i, j, 'L'))
        if not changes:
            break
        for change in changes:
            rows[change[1]] =rows[change[1]][:change[0]] + change[2] + rows[change[1]][change[0] + 1:]
    return rows

print(f"part1 {sum(1 for row in run(rows, one=True) for c in row if c == '#')}")
print(f"part2 {sum(1 for row in run(rows2) for c in row if c == '#')}")
