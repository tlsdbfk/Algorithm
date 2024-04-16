n = int(input())
array = list(map(int, input().split()))

start = 0
end = n

while start <= end:
    mid = (start + end) // 2

    if array[mid] == mid:
        answer = array[mid]
        break
    elif array[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
        
    answer = None

if answer == None:
    print(-1)
else:
    print(answer)