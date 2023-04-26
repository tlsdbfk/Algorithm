t = int(input())

for i in range(t):
    n = int(input())
    n_list = [(input()) for _ in range(n)]
    n_list.sort()
    flag = False

    for i in range(n-1):
        long = len(n_list[i])
        if n_list[i] == n_list[i+1][:long]:
            flag = True
            break

    if flag == True:
        print("NO")
    else:
        print("YES")