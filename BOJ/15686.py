n, m = map(int, input().split())

house =[]
chicken = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

from itertools import combinations

new_chicken = list(combinations(chicken, m))

min_value = int(1e9)

for cs in new_chicken:
    sum = 0
    for h in house:
        hx, hy = h
        dist = int(1e9)
        for c in cs:
            cx, cy = c
            dist = min(dist, abs(hx-cx) + abs(hy-cy))
        sum += dist

    min_value = min(min_value, sum)

print(min_value)