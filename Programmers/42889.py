def solution(N, stages):   
    count = 0 
    answer = []
    for i in range(N):
        if (len(stages)-count) == 0:
            answer.append((i+1, 0))
        else:
            answer.append((i+1, stages.count(i+1) / (len(stages)-count)))
        count += stages.count(i+1)
    sorted_answer = sorted(answer, key = lambda x:-x[1])
    
    result = []
    for answer in sorted_answer:
        result.append(answer[0])
    return result
