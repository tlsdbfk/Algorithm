start = input()

if start[0] == "a":
    x = 0
elif start[0] == "b":
    x = 1
elif start[0] == "c":
    x = 2
elif start[0] == "d":
    x = 3
elif start[0] == "e":
    x = 4
elif start[0] == "f":
    x = 5
elif start[0] == "g":
    x = 6
elif start[0] == "h":
    x = 7

y = int(start[1]) - 1

dx = [2, 2, -2, -2, -1, +1, -1, +1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        count += 1

print(count)
