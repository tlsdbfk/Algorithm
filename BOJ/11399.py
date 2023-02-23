n = int(input())
p = list(map(int, input().split()))

p.sort()

sum_list = [0] * n

sum_list[0] = p[0]

for i in range(1, n):
    sum_list[i] = sum_list[i-1] + p[i]

print(sum(sum_list))