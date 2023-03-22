from functools import cmp_to_key

k, n = map(int, input().split())
k_list = []
for i in range(k):
    k_list.append(int(input()))

def compare(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return -1
    else:
        return 1

max_num = max(k_list)

for _ in range(n - len(k_list)):
    k_list.append(max_num)
k_list = sorted(k_list, key = cmp_to_key(compare))

for k in k_list:
	print(k, end ='')