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

print(sum([getDist(x) for x in l.keys()]))
