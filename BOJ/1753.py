import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

v, e = map(int, input().split())
k = int(input())
inf = int(1e9)

graph = [[] * (v+1) for _ in range(v+1)]

distance = [inf] * (v+1)
# visited = [False] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(k)

for i in range(1, v+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])

'''
def get_smallest_node():
    min_val = inf
    index = 0
    for i in range(1, v+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i    
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for _ in range(v-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
'''