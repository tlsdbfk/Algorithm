n, m = map(int, input().split())

n_list = list(map(int, input().split()))
n_list.sort()

visited = [False] * n

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    overlap = 0

    for i in range(n):
        if not visited[i] and overlap != n_list[i]:
            visited[i] = True
            s.append(n_list[i])
            overlap = n_list[i]
            dfs()
            visited[i] = False
            s.pop()

dfs()