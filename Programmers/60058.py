def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ""

    if p == "":
        return answer

    index = balanced_index(p)

    u = p[:index+1]
    v = p[index+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"

        temp = u[1:-1]

        for i in range(len(temp)):
            if temp[i] == "(":
                answer += ")"
            else:
                answer += "("
    
    return answer


'''
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == "":
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        temp1 = u[1:-1]
        temp2 = ""
        
        for t in temp1:
            if t == "(":
                temp2 += ")"
            else:
                temp2 += "("
        answer = "(" + solution(v) + ")" + temp2
    return answer
'''
        
'''
        answer = "("
        answer += solution(v)
        answer += ")"
        
        u = list(u[1:-1])
        
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        
        answer += "".join(u)
    
    return answer
'''
