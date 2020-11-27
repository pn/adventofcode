#!/usr/bin/env python3
import math
rows = [x.strip() for x in open('input10.txt').readlines()]
asteroids = []
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col == '#':
            asteroids.append((x, y))


def vector(i, j):
    return j[0] - i[0], j[1] - i[1]


def normalize(v):
    magnitude = math.sqrt(v[0]**2 + v[1]**2)
    return v[0] / magnitude, v[1] / magnitude


def has_vector(v, vectors):
    for vec in vectors:
        if math.isclose(v[0], vec[0]) and math.isclose(v[1], vec[1]):
            return True
    return False


best = None
num_directions = 0
for station in asteroids:
    directions = set()
    for asteroid in asteroids:
        if asteroid == station:
            continue
        v = normalize(vector(station, asteroid))
        if not has_vector(v, directions):
            directions.add(v)
    if len(directions) > num_directions:
        best = station
        num_directions = len(directions)

print(f'best station {best} sees {num_directions} asteroids')
