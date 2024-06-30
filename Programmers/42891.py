import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    food_num = len(food_times)
    previous = 0
    
    while q:
        time = (q[0][0] - previous) * food_num
        
        if k >= time:
            k -= time
            previous = heapq.heappop(q)[0]
            food_num -= 1
        else:
            index = k % food_num
            q.sort(key=lambda x:x[1])
            answer = q[index][1]
            break
    return answer
