#!/usr/bin/env python3
l = dict([i.strip().split(')')[::-1] for i in open('input6.txt').readlines()])
dist = {}

def getDist(o):
    if o == 'COM':
        return 0
    if o in dist:
        return dist[o]
    else:
        dist[o] = getDist(l[o]) + 1
        return dist[o]

def getAll(o):
    r = []
    while l[o] != 'COM':
        r.append(l[o])
        o = l[o]
    return r
    
osan = getAll('SAN')
oyou = getAll('YOU')
D = None
for s in osan:
    for y in oyou:
        if y == s:
            D = s
            break # breaks two loops in this case
    else:
        continue # Continue if the inner loop wasn't broken.
    break # Inner loop was broken, break the outer.
print(getDist('SAN') + getDist('YOU') - 2 * getDist(D) - 2)
