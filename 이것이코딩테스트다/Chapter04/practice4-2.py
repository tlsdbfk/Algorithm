N = int(input())

count = 0
for i in range(0, 60):
    for j in range(0, 60):
        if "3" in (str(i)+str(j)):
            count += 1

if N < 3:
    print((N+1) * count)
else:
    print(N * count + 60*60)