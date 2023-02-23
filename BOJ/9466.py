import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

def dfs(x):
    global answer
    visited[x] = True
    cycle.append(x)
    num = arr[x]

    if visited[num]:
        if num in cycle:
            answer += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    answer = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(answer))