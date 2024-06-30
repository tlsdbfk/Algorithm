def rotate(key):
    m = len(key)
    
    result = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            result[j][m-1-i] = key[i][j]
    
    return result

def check(new_lock):
    n = len(new_lock) // 3
    
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i] [j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        
        for x in range(2 * n):
            for y in range(2 * n):
                
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock):
                    return True
                
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[x+i][y+j] -= key[i][j]
    return False