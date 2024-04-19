n = int(input())

t = []
p = []

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

max_value = 0
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    end = i + t[i]

    if end <= n:
        dp[i] = max(max_value, dp[i + t[i]] + p[i])
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max(dp))