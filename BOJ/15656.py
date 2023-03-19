n, m = map(int, input().split())

n_list = list(map(int, input().split()))

n_list.sort()

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(0, len(n_list)):
        s.append(n_list[i])
        dfs()
        s.pop()

dfs()