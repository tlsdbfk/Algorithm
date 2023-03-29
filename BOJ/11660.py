import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = []
for i in range(n):
    n_list.append(list(map(int, (input().split()))))

dp = []
for i in range(n+1):
    dp.append([0] * (n+1))

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1] + n_list[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)
