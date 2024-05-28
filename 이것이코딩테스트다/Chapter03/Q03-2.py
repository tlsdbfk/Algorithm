n, m = map(int, input().split())

minlist = []

for _ in range(n):
    data = list(map(int, input().split()))
    minlist.append(min(data))

print(max(minlist))

result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)