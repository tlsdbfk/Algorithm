from collections import deque

n, m, k, x = map(int, input().split())

dist = [-1] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = x

dist[x] = 0

q = deque([x])
while q:
    now = q.popleft()

    for n in graph[now]:
        if dist[n] == -1:
            dist[n] = dist[now] + 1
            q.append(n)

check = False

for i in range(1, len(dist)):
    if dist[i] == k:
        print(i)
        check = True
    
if check == False:
    print(-1)
    