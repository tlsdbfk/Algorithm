n = int(input())

score = []

for i in range(n):
    score.append(list(input().split()))

sorted_score = sorted(score, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), str(x[0])))

for i in range(n):
    print(sorted_score[i][0])