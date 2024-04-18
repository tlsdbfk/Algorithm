'''
n, l, r = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

count = 0

while True:
    open = []

    for i in range(n):
        for j in range(n):
            for d in range(4):
                ni = di[d] + i
                nj = dj[d] + j
                if ni >= 0 and ni < n and nj >= 0 and nj < n:
                    if abs(board[ni][nj] - board[i][j]) >= l and abs(board[ni][nj] - board[i][j]) <= r:
                        open.append((i,j))
                        open.append((ni, nj))

    print(set(open))

    if not set(open):
        break

    count += 1

    sum = 0
    for x, y in set(open):
        print(x, y)
        sum += board[x][y]

    for x, y in set(open):
        board[x][y] = int(sum / len(set(open)))

    print(board)

print(count)

# 공유가 각각 될수도 있어서 이건 안 된다 ..

'''

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))

                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    
    for i in range(n):
        for j in range(n):

            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    if index == n * n:
        break

    total_count += 1

print(total_count)