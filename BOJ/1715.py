import heapq, sys
input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))

heapq.heapify(cards)
count = 0

while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    count += tmp
    
print(count)
