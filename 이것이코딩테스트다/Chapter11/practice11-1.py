n = int(input())
n_list = list(map(int, input().split()))
n_list = sorted(n_list)

count = 0

while True: 
    if len(n_list) == 0:
        break
    if n_list[-1]-1 > len(n_list):
        break

    for i in range(n_list[-1]-1):
        n_list.remove(n_list[i])
    n_list.remove(n_list[-1])

    count += 1

print(count)