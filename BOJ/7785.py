n = int(input())

name = {}

for i in range(n):
    a, b = map(str, input().split())
    name[a] = b

name = dict(sorted(name.items(), reverse=True))

for key, value in name.items():
    if value == "enter":
        print(key)