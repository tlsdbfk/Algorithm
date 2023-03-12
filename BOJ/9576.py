import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    wishlist = []

    for _ in range(M):
        wishlist.append(list(map(int, input().split())))
        wishlist = sorted(wishlist, key = lambda x:x[1])

        count = 0
        visited = [False] * (N+1)

        for a,b in wishlist:
            for i in range(a, b+1):
                if not visited[i]:
                    visited[i] = True
                    count += 1
                    break
    
    print(count)

