from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]


    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())

        if graph[a][b] == True:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    onlyone = True
    cycle = False

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            onlyone = False
            break
        
        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j] == True:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    
    if onlyone == False:
        print("?")
    
    elif cycle == True:
        print("IMPOSSIBLE")

    else:
        for i in result:
            print(i, end=" ")
        print()