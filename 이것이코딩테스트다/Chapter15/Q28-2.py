n = int(input())
array = list(map(int, input().split()))

start = 0
end = n-1

while start < end:
    mid = (start + end) // 2

    if array[mid] == mid:
        print(mid)
        break

    elif array[mid] < mid:
        start = mid + 1
    
    else:
        end = mid - 1
