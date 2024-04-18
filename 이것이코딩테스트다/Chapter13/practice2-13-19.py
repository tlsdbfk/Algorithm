n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(i, now, add, sub, mul, div):
    global max_value, min_value

    if i == n:
        max_value = max(now, max_value)
        min_value = min(now, min_value)
        return

    else:
        if add > 0:
            dfs(i+1, now + num[i], add-1, sub, mul, div)
        if sub > 0:
            dfs(i+1, now - num[i], add, sub-1, mul, div)
        if mul > 0:
            dfs(i+1, now * num[i], add, sub, mul-1, div)
        if div > 0:
            dfs(i+1, int(now / num[i]), add, sub, mul, div-1)

dfs(1, num[0], add, sub, mul, div)

print(max_value)
print(min_value)