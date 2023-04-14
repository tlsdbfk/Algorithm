import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    n_list = []

    for _ in range(n):
        n_list.append(list(map(int, input().split())))

    n_list.sort()
    
    tmp = n_list[0][1]
    count = 1

    for i in range(0, len(n_list)):
        if tmp > n_list[i][1]:
            count += 1
            tmp = n_list[i][1]

    print(count)
    '''

    for i in range(len(n_list)-1):
        if n_list[i][1] < n_list[i+1][1]:
            count += 1
        i += 1
    print(n - count)
    '''