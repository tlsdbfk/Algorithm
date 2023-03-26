'''
n, m = map(int, (input().split()))

n_list = [0] * (n+1)

for i in range (1, n+1):
    n_list[i] = int(input())

for j in range(m):
    a, b = map(int, input().split())
    temp_list = n_list[a:b+1]
    print(min(temp_list))
'''