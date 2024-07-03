from collections import deque

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

s, target_x, target_y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

virus.sort()
q = deque(virus)

while q:
    num, time, x, y = q.popleft()

    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = num
                q.append((num, time + 1, nx, ny))

print(graph[target_x-1][target_y-1])