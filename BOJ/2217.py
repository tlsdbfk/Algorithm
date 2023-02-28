n = int(input())

w = []

for i in range(n):
    w.append(int(input()))

w.sort(reverse=True)
result = []

for i in range(n):
    result.append(w[i] * (i+1))

print(max(result))

''' 
# 시간초과
max_weight = max(max(w), n * min(w))

for i in range(2, n):
    for j in range(1, n-1):
        max_weight = max(max_weight, i * w[j])

print(max_weight)
'''