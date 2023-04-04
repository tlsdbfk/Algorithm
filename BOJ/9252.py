import sys
input = sys.stdin.readline

a = [""] + list(input().rstrip())
b = [""] + list(input().rstrip())

dp = []
for _ in range(len(b)):
    dp.append([""]*(len(a)))

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1] + a[j]
        else:
            if len(dp[i][j-1]) >= len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

print(len(dp[-1][-1]))
print(dp[-1][-1])