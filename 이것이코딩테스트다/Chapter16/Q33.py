n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    end = t[i] + i

    if end <= n:
        dp[i] = max(p[i] + dp[t[i] + i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)