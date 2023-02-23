k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    # print(a ** b % 10)

    aa = a % 10

    if aa == 0:
        print(10)

    elif aa == 1 or aa == 5 or aa == 6:
        print(aa)

    elif aa == 4 or aa == 9:
        bb = b % 2
        if bb == 1:
            print(aa % 10)
        else:
            print(aa * aa % 10)
    else:
        bb = b % 4
        if bb == 0:
            print(aa ** 4 % 10)
        else:
            print(aa ** bb % 10)