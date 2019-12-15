#!/usr/bin/env python3
from math import gcd
moon_pos = []
for line in open('input12.txt').readlines():
    line = line.strip()
    line = line.strip('<>')
    coords = []
    for part in line.split(','):
        coords.append(int(part.split('=')[1].strip()))
    moon_pos.append(coords)
num_moons = len(moon_pos)


def cycle_length(pos, vel):
    length, orig_pos, orig_vel = 0, pos.copy(), vel.copy()
    moon_pairs = [(i, j) for i in range(num_moons) for j in range(num_moons) if j > i]
    while not length or pos != orig_pos or vel != orig_vel:
        for moon1, moon2 in moon_pairs:
            diff = pos[moon1] - pos[moon2]
            diff = diff // abs(diff) if diff else 0
            vel[moon1] += -diff
            vel[moon2] += diff
        for moon in range(num_moons):
            pos[moon] += vel[moon]
        length += 1
    return length


def lcm(a, b): return a * b // gcd(a, b)


px, py, pz = [list(x) for x in zip(*moon_pos)]
vx, vy, vz = [0] * num_moons, [0] * num_moons, [0] * num_moons
print(lcm(cycle_length(px, vy), lcm(cycle_length(py, vy), cycle_length(pz, vz))))
