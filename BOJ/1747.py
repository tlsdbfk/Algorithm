import math

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

n = int(input())

while True:
    if isPrime(n) and isPalindrome(n):
        print(n)
        break
    n += 1