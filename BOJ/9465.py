T = int(input())

for _ in range(T):
    n = int(input())
    
    n_list = []

    for i in range(2):
        n_list.append(list(map(int, input().split())))

    dp = []

    for i in range(2):
        dp.append([0] * n)
    
    for i in range(n):
        for j in range(2):
            if i == 0:
                dp[j][i] = n_list[j][i]
            if i == 1:
                dp[j][i] = dp[1-j][i-1] + n_list[j][i]
            if i >= 2:
                dp[j][i] = max(dp[1-j][i-1], dp[1-j][i-2]) + n_list[j][i]
    
    print(max(dp[1][n-1], dp[0][n-1]))
