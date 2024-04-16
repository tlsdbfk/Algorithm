n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = triangle

for i in range(len(dp)-2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])