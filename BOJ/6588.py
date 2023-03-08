import sys
input = sys.stdin.readline

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i] == True:
        for j in range(i+i, 1000001, i):
            array[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break
    else:
        print("Goldbach's conjecture is wrong.")