N = int(input())

name_list = []
score_list = []

for i in range(N):
    name, score = map(str, input().split())
    name_list.append(name)
    score_list.append(int(score))

sorted_score_list = sorted(score_list)

for s in sorted_score_list:
    index = score_list.index(s)
    print(name_list[index], end=' ')