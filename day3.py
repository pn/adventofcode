#!/usr/bin/env python3
result = 0
f = open('input3.txt')
w1i = f.readline()
w2i = f.readline()
w1 = [x.strip() for x in w1i.split(',')]
w2 = [x.strip() for x in w2i.split(',')]
a, b = [], []
a1 = [ [ 0 for y in range( 1000 ) ] for x in range( 1000 ) ]
a2 = [ [ 0 for y in range( 1000 ) ] for x in range( 1000 ) ]
wz1 = []
wz2 = []
for w in w1:
    wz1.append((w[:1], int(w[1:])))
for w in w2:
    wz2.append((w[:1], int(w[1:])))
p1 = []
p2 = []
def getMove(move):
    if move == 'U':
        return (0, 1)
    elif move == 'D':
        return (0, -1)
    elif move == 'R':
        return (1, 0)
    elif move == 'L':
        return (-1, 0)

def points(a):
    x, y = 0, 0
    result = []
    for d, l in a:
        m = getMove(d)
        for i in range(l):
            x += m[0]
            y += m[1]
            result.append((x, y))
    return result
s1 = set(points(wz1))
s2 = set(points(wz2))
comm = s1.intersection(s2)
cross = []


# count crossing
m = 1000000000
for c in comm:
    z = abs(c[0]) + abs(c[1])
    if z < m:
        m = z
        
print(comm)
print(m)
