n, k = map(int, input().split())

n_list = [[0, 0]]

#dp = [[0] * (k+1) for _ in range(n+1)]

dp = []

for i in range(n+1):
    dp.append([0] * (k+1))

for i in range(n):
    n_list.append(list(map(int, input().split())))

for i in range(1, n+1):
    w = n_list[i][0]
    v = n_list[i][1]

    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[n][k])