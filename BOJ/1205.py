n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    n_list = list(map(int, input().split()))
    if n == p and n_list[-1] >= score:
        print(-1)
    else:
        n_list.append(score)
        n_list.sort(reverse=True)
        print(n_list.index(score)+1)