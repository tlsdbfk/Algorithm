n, k = map(int, input().split())

n_list = []

for i in range(n):
    n_list.append(int(input()))

answer = 0

for i in range(n-1, -1, -1):

    if k == 0:
        break

    num = k // n_list[i]
    k = k % n_list[i]
    
    answer = answer + num

print(answer)