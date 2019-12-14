#!/usr/bin/env python3
moon_pos = []
moon_vel = []
for line in open('input12.txt').readlines():
    line = line.strip()
    line = line.strip('<>')
    coords = []
    for part in line.split(','):
        coords.append(int(part.split('=')[1].strip()))
    moon_pos.append(coords)
    moon_vel.append([0] * 3)


def get_energy(pos, vel, steps):
    num_moons = len(pos)
    for step in range(steps):
        moon_pairs = list(filter(lambda x: x[0] != x[1], [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]))
        for moon1, moon2 in moon_pairs:
            for axis in range(3):
                diff = pos[moon1][axis] - pos[moon2][axis]
                if diff != 0:
                    diff = diff // abs(diff)
                vel[moon1][axis] += -diff
                vel[moon2][axis] += diff

        for moon in range(num_moons):
            for i in range(3):
                pos[moon][i] += vel[moon][i]
    total = 0
    for moon in range(num_moons):
        pot, kin = 0, 0
        for i in range(3):
            pot += abs(pos[moon][i])
            kin += abs(vel[moon][i])
        total += pot * kin
    return total


print(get_energy(moon_pos.copy(), moon_vel.copy(), steps=1000))

