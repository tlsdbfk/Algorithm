n, m = map(int, input().split())
k = list(map(int, input().split()))

count = 0
for i in range(n-1):
    for j in range(1, n):
        if k[i] != k[j] and i < j:
            count += 1

print(count)

# -------------------------------------- #

array = [0] * 11

for x in k:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)