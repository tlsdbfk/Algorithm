import sys
import heapq

input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(n_list, (a, b))

l, p = map(int, input().split())

count = 0
temp_list = []

while p < l:
    while n_list and n_list[0][0] <= p:
        a, b = heapq.heappop(n_list)
        heapq.heappush(temp_list, (-b, a))

    if not temp_list:
        count = -1
        break

    b, a = heapq.heappop(temp_list)
    p = p + (-b)
    count += 1

print(count)