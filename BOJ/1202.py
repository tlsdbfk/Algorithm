import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []

for i in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))

bags = []

for i in range(k):
    bags.append(int(input()))

bags.sort()

temp_jewel=[]
answer = 0

for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp_jewel, -heapq.heappop(jewel)[1])
    if temp_jewel:
        answer += (-heapq.heappop(temp_jewel))
    elif not jewel:
        break

print(answer)