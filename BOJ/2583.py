import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global num
    num += 1
    board[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > -1 and nx < m and ny > -1 and ny < n:
            if board[nx][ny] == 0:
                dfs(nx, ny)

m, n, k = map(int, input().split())

board = [[0] * n for i in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

numlist = []

for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            num = 0
            dfs(i, j)
            numlist.append(num)

print(len(numlist))
for i in sorted(numlist):
    print(i,end = " ")