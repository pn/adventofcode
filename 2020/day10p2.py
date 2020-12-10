adapters, arrangements = [], {}
for line in open('input10.txt').read().splitlines():
    adapters.append(int(line))
adapters = list(reversed(sorted(adapters + [0])))

for current in adapters:
    all_compatible = [a for a in adapters if 0 < a - current <= 3]
    arrangements[current] = sum(arrangements[adapter] for adapter in all_compatible) if all_compatible else 1
print(arrangements[0])
