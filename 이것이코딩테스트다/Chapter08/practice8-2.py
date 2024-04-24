x = int(input())
count = 0
while (x != 1):
    if x % 5 == 0:
        x = x // 5
    elif x % 3 == 0:
        x = x // 3
    elif x % 2 == 0:
        x = x // 2
    else:
        x = x - 1
    print(x)
    count += 1

print(count)