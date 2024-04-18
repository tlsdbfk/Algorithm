n, m = map(int, input().split())

array = []
for i in range(n):
    num_list = list(map(int, input().split()))
    num_list.sort()
    array.append(num_list)

max_value = -100001

for i in range(n):
    max_value = max(array[i][0], max_value)

print(max_value)

