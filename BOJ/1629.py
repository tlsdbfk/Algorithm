import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def devide_conquer(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = devide_conquer(a, b // 2, c)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

print(devide_conquer(a, b, c))