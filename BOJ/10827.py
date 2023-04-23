a, b = list(input().split())

p = a.split(".")
p = int(len(p[1]))
a = a.replace(".", "")

result = str(int(a) ** int(b))
p = str((10 ** p) ** int(b))

index = len(result) - (len(p) - 1)

if index >= 0:
    print(result[:index] + '.' + result[index:])
else:
    print('0.' + '0' * (-index) + result)