n = int(input())

score_list = []

for _ in range(n):
    score_list.append(list(input().split()))

score_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for data in score_list:
    print(data[0])