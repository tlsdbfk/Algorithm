'''
n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

check = [[False] * n for _ in range(n)]

s, x, y = map(int, input().split())

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

def dfs(a, b, j):
    for i in range(4):
        na = da[i] + a
        nb = db[i] + b

        if na >= 0 and na < n and nb >= 0 and nb < n:
            if graph[na][nb] == 0 and check[na][nb] == False:
                graph[na][nb] = j
                check[na][nb] = True

for i in range(s): # 1, 2, 3초
    check = [[False] * n for _ in range(n)]
    for j in range(1, k+1): # 바이러스 1, 2, 3 마다
        for a in range(n):
            for b in range(n): # 다 돌면서 각 바이러스면서 해당 초에 간 적이 없는 경우
                if graph[a][b] == j and check[a][b] == False:
                    check[a][b] = True
                    dfs(a, b, j)

print(graph[x-1][y-1])
'''
from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, s, x, y = q.popleft()

    if s == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus

                q.append((virus, s+1, nx, ny))

print(graph[X-1][Y-1])