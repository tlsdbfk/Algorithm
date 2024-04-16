n, x = map(int, input().split())
array = list(map(int, input().split()))

# array 에서 x 가 처음으로 등장하는 인덱스 구하기
def first(array, x, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if (mid == 0 or array[mid-1] < x) and array[mid] == x: # x가 가장 왼쪽에 나올 경우의 인덱스 
        return mid
    elif array[mid] >= x: # x 보다 현재의 중간값이 크거나 같으면 왼쪽 부분 탐색
        return first(array, x, start, mid-1)
    else: # x 보다 현재의 중간값이 작으면 오른쪽 부분 탐색
        return first(array, x, mid+1, end)

# array 에서 x 가 마지막으로 등장하는 인덱스 구하기
def last(array, x, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if (mid == n-1 or array[mid+1] > x) and array[mid] == x: # 가장 오른쪽에 있는 x의 인덱스 반환
        return mid
    elif array[mid] > x: # 현재의 값이 x 보다 크면 왼쪽 탐색
        return last(array, x, start, mid-1)
    else: # 현재의 값이 x 보다 작거나 같으면 오른쪽 탐색
        return last(array, x, mid + 1, end)

# x가 가장 마지막으로 등장한 인덱스 - 가장 처음으로 등장한 인덱스 + 1 이 x의 개수
def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)

    if a == None:
        return 0
    
    b = last(array, x, 0, n-1)

    return b-a+1

result = count_by_value(array, x)

if result == 0:
    print(-1)
else:
    print(result)