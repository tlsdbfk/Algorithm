'''
n = int(input())
direction = input().split()

x = 0
y = 0

for d in direction:
    if d == "L":
        if y-1 >= 0:
            y -= 1
    if d == "R":
        if y+1 < n:
            y += 1
    if d == "U":
        if x-1 >= 0:
            x -= 1
    if d == "D":
        if x+1 < n:
            x += 1

print(x+1, y+1)
'''

n = int(input())

x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(4):
        if plan == direction[i]:
            nx = dx[i] + x
            ny = dy[i] + y
        
    if nx < 1 or nx >n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(x, y)