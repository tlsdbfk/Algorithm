a, b = map(int, input().split())

result = 1
result2 = 1

for i in range(b):
    result *= (a-i)

for i in range(1, b+1):
    result2 *= i

print(result // result2)