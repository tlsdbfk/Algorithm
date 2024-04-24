N, M = map(int, input().split())

#check = []
#for _ in range(N):
#    check.append([0] * M)

check = [[0] * M for _ in range(N)]

x, y, d = map(int, input().split())

check[x][y] = 1

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

#     북, 동, 남, 서
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn_count = 0

while True:
    turn_left()

    nx = x + dx[d]
    ny = y + dy[d]

    if check[nx][ny] == 0 and array[nx][ny] == 0:
        check[nx][ny] = 1

        x = nx
        y = ny

        count += 1
        turn_count = 0

        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(count)