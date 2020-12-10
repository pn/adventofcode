adapters = []
for line in open('input10.txt').read().splitlines():
    adapters.append(int(line))
adapters.append(max(adapters) + 3)  # device adapter
numjolts = {1: 0, 2: 0, 3: 0}

current = 0
while current != max(adapters):
    selected = min(adapter for adapter in adapters if 0 < adapter - current <= 3)
    numjolts[selected - current] += 1
    current = selected

print(numjolts[1] * numjolts[3])
