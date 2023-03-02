k, n = map(int, input().split())

k_list = []

for i in range(k):
    k_list.append(int(input()))

start = 1
end = max(k_list)

while start <= end:
    mid = (start + end) // 2

    result = 0

    for i in k_list:
        if i >= mid:
            result += i // mid
    
    if result >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)