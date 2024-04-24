N, K = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list = sorted(A_list)
B_list = sorted(B_list, reverse=True)

for i in range(K):
    A_list[i] = B_list[i]

print(sum(A_list))