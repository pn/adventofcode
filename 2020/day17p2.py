lines = [line for line in open('input17.txt').read().splitlines() if line]
active = {}
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        if cell == '#':
            active[(x, y, 0, 0)] = True

rel_neighbours = [(x, y, z, a) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1) for a in (-1, 0, 1)]
rel_neighbours.remove((0, 0, 0, 0))
dim = 4

def active_neighbours(active, position, max_i = None):
    result = 0
    min_dim = [0 for _ in range(dim)]
    max_dim = [0 for _ in range(dim)]
    for pos in active:
        for d in range(dim):
            min_dim[d] = min(min_dim[d], pos[d])
            max_dim[d] = max(max_dim[d], pos[d])
    checked = []
    for rel_pos in rel_neighbours:
        neigbhour_pos = list(position[i] + rel_pos[i] for i in range(dim))
        np = tuple(neigbhour_pos)
        if np in active:
            result += 1
        if result >= max_i:
            break
        checked.append(np)
    return result

def process_inactive(active):
    changes = {}
    min_dim = [0 for d in range(dim)]
    max_dim = [0 for d in range(dim)]
    for pos in active:
        for d in range(dim):
            min_dim[d] = min(min_dim[d], pos[d])
            max_dim[d] = max(max_dim[d], pos[d])
    for x in range(min_dim[0] - 1, max_dim[0] + 2):
        for y in range(min_dim[1] - 1, max_dim[1] + 2):
            for z in range(min_dim[2] - 1, max_dim[2] + 2):
                for a in range(min_dim[3] - 1, max_dim[3] + 2):  # TODO make dim dependent
                    pos = (x, y, z, a)
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
