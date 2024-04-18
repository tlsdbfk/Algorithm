n, m = map(int, input().split())
weight = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            count += 1

print(count)