'''
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

list0 = []
list2 = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            list0.append([i, j])
        elif graph[i][j] == 2:
            list2.append([i, j])

print(list0)
print(list2)

def BFS(graph, list2):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([x, y])

    while q:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append([graph[nx], graph[ny]])
    
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[x][y] == 0:
                count += 1
    
    return count

wall_list = list(combinations(list0, 3))

answer = 100

for wall in wall_list:
    print(wall)
    for w in wall:
        x, y = w
        graph[x][y] = 1
        answer = min(answer, BFS(graph, list2))

print(answer)
'''

n, m = map(int, input().split())

data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
