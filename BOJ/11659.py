n, m = map(int, input().split())
num = list(map(int, input().split()))

def prefix_sum(n):
    prefixSum = [0] * (n+1)
    prefixSum[0] = 0

    for i in range(1, n+1):
        prefixSum[i] = prefixSum[i-1] + num[i-1]

    return prefixSum

prefixSum = prefix_sum(n)

result = []

for _ in range(m):
    i, j = map(int, input().split())

    result.append(prefixSum[j] - prefixSum[i-1]) 

for r in result:
    print(r)