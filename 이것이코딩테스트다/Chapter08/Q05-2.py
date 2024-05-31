n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

dp = [10001] * (m+1)

dp[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[j] != 10001:
    print(dp[j])
else:
    print(-1)