n, k = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))

n_list.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(len(n_list)):
    if n_list[i][0] == k:
        index = i

for i in range(len(n_list)):
    if n_list[index][1:] == n_list[i][1:]:
        print(i+1)
        break