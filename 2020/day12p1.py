instructions = [(line[0], int(line[1:])) for line in open('input12.txt').read().splitlines()]
world_directions = ['N', 'E', 'S', 'W']
position = [0, 0]
direction = 'E'

def move(pos, dir, val):
    if dir == 'E':
        pos[0] += val
    elif dir == 'W':
        pos[0] -= val
    elif dir == 'N':
        pos[1] -= val
    elif dir == 'S':
        pos[1] += val
    return pos

def turn(dir, right, degrees):
    i = world_directions.index(dir)
    return world_directions[(4 + i + (1 if right else -1) * (degrees // 90)) % 4]

for inst in instructions:
    if inst[0] in world_directions:
        position = move(position, inst[0], inst[1])
    elif inst[0] == 'F':
        position = move(position, direction, inst[1])
    elif inst[0] in ['L', 'R']:
        direction = turn(direction, inst[0] == 'R', inst[1])

print(abs(position[0]) + abs(position[1]))
