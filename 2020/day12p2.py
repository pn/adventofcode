instructions = [(line[0], int(line[1:])) for line in open('input12.txt').read().splitlines()]
world_directions = ['N', 'E', 'S', 'W']
position = [0, 0]
waypoint = [10, -1]

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

def rotate(wayp, right, degrees):
    r = (4 + (1 if right else -1) * (degrees // 90)) % 4
    if r == 2:
        return [-wayp[0], -wayp[1]]
    elif r == 1:
        return [-wayp[1], wayp[0]]
    elif r == 3:
        return [wayp[1], -wayp[0]]
    return wayp

for inst in instructions:
    if inst[0] in world_directions:
        waypoint = move(waypoint, inst[0], inst[1])
    elif inst[0] == 'F':
        position[0] += inst[1] * waypoint[0]
        position[1] += inst[1] * waypoint[1]
    elif inst[0] in ['L', 'R']:
        waypoint = rotate(waypoint, inst[0] == 'R', inst[1])

print(abs(position[0]) + abs(position[1]))
