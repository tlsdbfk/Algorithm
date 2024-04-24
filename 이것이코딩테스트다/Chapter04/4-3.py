input_data = input()

if input_data[0] == "a":
    x = 1
elif input_data[0] == "b":
    x = 2
elif input_data[0] == "c":
    x = 3
elif input_data[0] == "d":
    x = 4
elif input_data[0] == "e":
    x = 4
elif input_data[0] == "f":
    x = 5
elif input_data[0] == "g":
    x = 7
elif input_data[0] == "h":
    x = 8

y = int(input_data[1])

dx = [+2, +2, -2, -2, +1, -1, +1, -1]
dy = [+1, -1, +1, -1, +2, +2, -2, -2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
        count += 1

print(count)