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
    result = {}
    ll = 0
    for d, l in a:
        m = getMove(d)
        for i in range(l):
            x += m[0]
            y += m[1]
            ll += 1
            if (x, y) not in result:
                result[(x, y)] = ll
    return result
p1 = points(wz1)
p2 = points(wz2)
s1 = set(p1.keys())
s2 = set(p2.keys())
comm = s1.intersection(s2)
cross = []

m = 1000000000
for c in comm:
    z = p1[c] + p2[c]
    if z < m:
        m = z
        
print(m)
