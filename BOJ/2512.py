n = int(input())
n_list = list(map(int, input().split()))
m = int(input())

start = 1
end = max(n_list)

while start <= end:
    mid = (start + end) // 2

    result = 0

    for i in n_list:
        if i > mid:
            result += mid
        else:
            result += i

    if result <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)