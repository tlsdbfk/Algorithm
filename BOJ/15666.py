n, m = map(int, input().split())

n_list = list(map(int, input().split()))
n_list.sort()

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    overlap = 0

    for i in range(start, n):
        if overlap != n_list[i]:
            s.append(n_list[i])
            overlap = n_list[i]
            dfs(i)
            s.pop()

dfs(0)