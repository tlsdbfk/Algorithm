n, m = map(int, input().split())

n_list = list(map(int, input().split()))
n_list.sort()

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    overlap = 0

    for i in range(n):
        if overlap != n_list[i]:
            s.append(n_list[i])
            overlap = n_list[i]
            dfs()
            s.pop()

dfs()