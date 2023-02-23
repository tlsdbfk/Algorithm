n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))


'''
answer = []
result = 0

for j in range(0, n):
    answer.append(a_list[j])
    for i in range(j+1, n):
        if a_list[i] > a_list[i-1]:
            answer.append(a_list[i])   
        result = max(result, len(answer))
    answer = []

print(result)
'''