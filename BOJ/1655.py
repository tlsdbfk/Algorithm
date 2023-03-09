import sys
import heapq

input = sys.stdin.readline

heapA = []
heapB = []

n = int(input())

for i in range(n):
    x = int(input())
    if len(heapA) == len(heapB):
        heapq.heappush(heapA, (-x))
    else:
        heapq.heappush(heapB, x)
    if not heapB:
        print(-heapA[0])
        continue
    if -heapA[0] > heapB[0]:
        tempA = -1 * (heapq.heappop(heapA))
        tempB = heapq.heappop(heapB)
        heapq.heappush(heapA, -tempB)
        heapq.heappush(heapB, tempA)
    print(-heapA[0])