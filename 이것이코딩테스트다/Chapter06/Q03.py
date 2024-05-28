n = int(input())

array = []

for _ in range(n):
    name, score = map(str, input().split())
    array.append((name, int(score)))

array = sorted(array, key=lambda x : x[1])

for x in array:
    name, score = x
    print(name, end=" ")