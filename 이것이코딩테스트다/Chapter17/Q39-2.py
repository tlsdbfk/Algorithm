import heapq

t = int(input())

for _ in range(t):
    n = int(input())

    array = []
    for _ in range(n):
        array.append(list(map(int, input().split())))

    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    x, y = 0, 0
    q = [(array[0][0], x, y)]
    distance[x][y] = array[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            cost = dist + array[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
            
print(distance[n-1][n-1])