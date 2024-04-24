move = str(input())

if move[0] == "a":
    x = 1
elif move[0] == "b":
    x = 2
elif move[0] == "c":
    x = 3
elif move[0] == "d":
    x = 4
elif move[0] == "e":
    x = 5
elif move[0] == "f":
    x = 6
elif move[0] == "g":
    x = 7
elif move[0] == "h":
    x = 8

count = 0

dx = [2, 2, -2, -2, -1, +1, -1, +1]
dy = [-1, +1, -1, +1, 2, 2, -2, -2]

for i in range(8):
    nx = x + dx[i]
    ny = int(move[1]) + dy[i]

    if nx > 0 and ny > 0 and nx < 9 and ny < 9:
        count += 1

print(count)
