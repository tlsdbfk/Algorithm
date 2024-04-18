from itertools import combinations

n = int(input())

board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))
        if board[i][j] == "X":
            spaces.append((i, j))

def check(x, y, direction): # 선생님이 잡았을 때
    if direction == 0: # 왼쪽
        while y >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y -= 1
    
    if direction == 1: # 오른쪽
        while y < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y += 1

    if direction == 2: # 위쪽
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x -= 1

    if direction == 3: # 아래쪽
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x += 1

    return False

def procese():
    for x, y in teachers:
        for i in range(4):
            if check(x, y, i):
                return True # 선생님이 잡았을 때
    return False            

result = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = "O"
    
    if not procese(): # 선생님이 못 잡으면
        result = True 
        break

    for x, y in data:
        board[x][y] = "X"

if result:
    print("YES")
else:
    print("NO")