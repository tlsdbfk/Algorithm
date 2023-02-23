from collections import deque

height, width = map(int, input().split())
graph = []

for _ in range(height):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

def bfs():

    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < height and 0 <= ny < width and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    count += 1
    answer.append(count)
    return count

time = 0
while 1:
    visited = [[0] * width for _ in range(height)]
    cnt = bfs()
    if cnt == 0:
        break
    time += 1

print(time)
print(answer[-2])