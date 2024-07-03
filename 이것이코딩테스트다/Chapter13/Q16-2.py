from itertools import combinations
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

virus = []
blank = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

result = 0

def bfs(temp_graph):
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    q.append((nx, ny))

    global result

    count = 0

    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                count += 1
    
    result = max(result, count)

def iterate():
    new_wall_list = combinations(blank, 3)

    for walls in new_wall_list:
        a, b, c = walls[0], walls[1], walls[2]

        graph[a[0]][a[1]] = 1
        graph[b[0]][b[1]] = 1
        graph[c[0]][c[1]] = 1

        temp_graph = [data[:] for data in graph]
        bfs(temp_graph)

        graph[a[0]][a[1]] = 0
        graph[b[0]][b[1]] = 0
        graph[c[0]][c[1]] = 0

iterate()

print(result)
