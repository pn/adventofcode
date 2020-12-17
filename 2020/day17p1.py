lines = [line for line in open('input17.txt').read().splitlines() if line]
active = {}
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == '#':
            active[(x, y, 0)] = True

rel_neighbours = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
rel_neighbours.remove((0, 0, 0))

def active_neighbours(active, position, max_i = None):
    result = 0
    min_x = max_x = min_y = max_y = min_z = max_z = 0
    for pos in active:
        min_x = min(min_x, pos[0])
        max_x = max(max_x, pos[0])
        min_y = min(min_y, pos[1])
        max_y = max(max_y, pos[1])
        min_z = min(min_z, pos[2])
        max_z = max(max_z, pos[2])
    checked = []
    for rel_pos in rel_neighbours:
        neigbhour_pos = list(position[i] + rel_pos[i] for i in range(3))
        np = tuple(neigbhour_pos)
        if np in active:
            result += 1
        if result >= max_i:
            break
        checked.append(np)
    return result

def process_inactive(active):
    changes = {}
    min_x = max_x = min_y = max_y = min_z = max_z = 0
    for position in active:
        min_x = min(min_x, position[0])
        max_x = max(max_x, position[0])
        min_y = min(min_y, position[1])
        max_y = max(max_y, position[1])
        min_z = min(min_z, position[2])
        max_z = max(max_z, position[2])
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                pos = (x, y, z)
                if not active.get(pos, False):
                    if active_neighbours(active, pos, max_i=4) == 3:
                        changes[pos] = True
    return changes

def cycle(active):
    changes1 = {}
    for position in active:
        an = active_neighbours(active, position, max_i=4)
        if an not in [2, 3]:
            changes1[position] = False
    changes1.update(process_inactive(active))
    for change_pos in changes1:
        activate = changes1[change_pos]
        if activate:
            active[change_pos] = True
        else:
            del active[change_pos]

for i in range(6):
    cycle(active)

print(len(active))
