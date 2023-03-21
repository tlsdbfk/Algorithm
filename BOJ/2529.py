k = int(input())
k_list = list(map(str, input().split()))

visited = [False] * 10
max_ans = ""
min_ans = ""

def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j
    
def solve(start, s):
    global max_ans, min_ans

    if start == k+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s    
        return

    for i in range(10):
        if visited[i] == False:
            if (start == 0 or check(s[-1], str(i), k_list[start-1])):
                visited[i] = True
                solve(start+1, s+str(i))
                visited[i] = False

solve(0, "")
print(max_ans)
print(min_ans)