n = int(input())

room = []

for i in range(n):
    room.append(list(map(str, input())) + ["X"])
room.append(["X" for _ in range(n+1)])

result1, result2 = 0, 0
for i in range(n+1):
    tmp1, tmp2 = 0, 0
    for j in range(n+1):
        if room[i][j] == ".":
            tmp1 += 1
        elif room[i][j] == "X":
            if tmp1 >= 2:
                result1 += 1
            tmp1 = 0
            
        if room[j][i] == ".":
            tmp2 += 1
        elif room[j][i] == "X":
            if tmp2 >= 2:
                result2 += 1
            tmp2 = 0

print(result1, result2)