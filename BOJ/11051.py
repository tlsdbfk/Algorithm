import math
n, k = map(int, input().split())

#result = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

dp = [[1] * (i+1) for i in range(n+1)]

for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

result = dp[n][k]

print(result % 10007)