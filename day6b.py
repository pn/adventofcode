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
for o in osan:
    for oy in oyou:
        if oy == o:
            D = o
            break
    else:
        continue
    break
print(getDist('SAN') + getDist('YOU') - 2 * getDist(D) - 2)
