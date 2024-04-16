n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

dp = [10001] * (m+1)

dp[0] = 0

for x in array:
    for i in range(x, m+1):
        dp[i] = min(dp[i], dp[i-x] + 1)

if dp[m] != 10001:
    print(dp[m])
else:
    print(-1)