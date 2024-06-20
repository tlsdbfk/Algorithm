n = int(input())

array = [[0] * (n) for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    array[a-1][b-1] = 1

task = []
L = int(input())
for _ in range(L):
    a, b = map(str, input().split())
    task.append([int(a), b])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0
x, y = 0, 0
count = 0
q = [(x, y)]
array[x][y] = 2
index = 0

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx >= 0 and nx < n and ny >= 0 and ny < n and array[nx][ny] != 2:
        if array[nx][ny] == 0:
            array[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            array[px][py] = 0
        if array[nx][ny] == 1:
            array[nx][ny] = 2
            q.append((nx, ny))
    else:
        count += 1
        break

    x, y = nx, ny
    count += 1

    if index < L and count == task[index][0]:
        task_direction = task[index][1]

        if task_direction == "D":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        index += 1
    
print(count)
